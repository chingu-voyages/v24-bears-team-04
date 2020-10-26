from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Candidate
from .forms import VoteForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

class CandidateListView(ListView):
    model = Candidate
    template_name = 'candidate_list.html'
    fields = ['name']
    
    def form_valid(self, form):        
        return super().form_valid(form)

def vote(request):
    form = VoteForm()
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            try:
                candidate = Candidate.objects.get(name=request.POST.get('name'))
            except Candidate.DoesNotExist:
                candidate = Candidate(name=request.POST.get('name'))
            candidate.votes = candidate.votes + 1
            candidate.save()
            context = {'candidate': candidate.name}
            return HttpResponse("Your vote has been confirmed.")
        else:
            return HttpResponse("There was an error with your vote.")
    context = {'form': form}
    return render(request, 'vote.html', context)


# flask vote resource

# class Vote(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument("candidate_name", type=str)

#     def post(self):
#         data = Vote.parser.parse_args()
#         candidate_name = data["candidate_name"]
#         candidate = CandidateModel.find_by_name(name=candidate_name)
#         if not candidate:
#             candidate = CandidateModel(name=candidate_name)
#         candidate.votes = candidate.votes + 1
#         candidate.save_to_db()
#         return {"candidate name": candidate.name, "votes": candidate.votes}

#     def get(self):
#         candidates = CandidateModel.query.all()
#         json = []
#         for candidate in candidates:
#             json.append(candidate.json())
#         return json
