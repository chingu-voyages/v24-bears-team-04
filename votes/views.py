from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ElectionSerializer, UserSerializer, CandidateSerializer
from .decorators import unauthenticated_user, official_only
from .models import Candidate, Election, User
from .forms import UserCreationForm


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='login')
def vote(request, pk):
    user = User.objects.get(id=request.user.pk)
    if (user.elections.all().filter(pk=pk).exists()):
        return HttpResponse('You have already voted in this election.')
    election = Election.objects.get(id=pk)
    candidates = election.candidate_set.all()
    if request.method == 'POST':
        candidate = Candidate.objects.get(id=request.POST['candidate'])
        candidate.votes = candidate.votes + 1
        candidate.save()
        user.elections.add(election)
        return HttpResponse("Your vote has been confirmed.")
    context = {'election': election, 'candidates': candidates}
    return render(request, 'vote.html', context)

def logout(request):
	auth.logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
	user = request.user
	context = {'user': user}
	return render(request, 'home.html', context)

@unauthenticated_user
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def electionList(request):
    elections = Election.objects.all()
    serializer = ElectionSerializer(elections, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def electionDetail(request, pk):
    election = Election.objects.get(id=pk)
    serializer = ElectionSerializer(election, many=False)
    return Response(serializer.data)

@login_required(login_url='login')
@official_only
@api_view(['POST'])
def electionCreate(request):
    serializer = ElectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@login_required(login_url='login')
@official_only
@api_view(['POST'])
def electionUpdate(request, pk):
    election = Election.objects.get(id=pk)
    serializer = ElectionSerializer(instance=election, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@login_required(login_url='login')
@official_only
@api_view(['DELETE'])
def electionDelete(request, pk):
    election = Election.objects.get(id=pk)
    election.delete()
    return Response('The election has been deleted.')

@api_view(['GET'])
def electionCandidateList(request, pk):
    election = Election.objects.get(id=pk)
    candidates = election.candidate_set.all()
    serializer = CandidateSerializer(candidates, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def candidateList(request):
    candidates = Candidate.objects.all()
    serializer = CandidateSerializer(candidates, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def candidateDetail(request, pk):
    candidate = Candidate.objects.get(id=pk)
    serializer = CandidateSerializer(candidate, many=False)
    return Response(serializer.data)

@login_required(login_url='login')
@official_only
@api_view(['POST'])
def candidateCreate(request):
    serializer = CandidateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@login_required(login_url='login')
@official_only
@api_view(['POST'])
def candidateUpdate(request, pk):
    candidate = Candidate.objects.get(id=pk)
    serializer = CandidateUpdate(instance=candidate, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        Response('There was an error with your update.')
    return Response(serializer.data)

@login_required(login_url='login')
@official_only
@api_view(['DELETE'])
def candidateDelete(request, pk):
    candidate = Candidate.objects.get(id=pk)
    candidate.delete()
    return Response('The candidate has been deleted.')

@login_required(login_url='login')
@official_only
@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@login_required(login_url='login')
@api_view(['POST'])
def userUpdate(request):
    user = User.objects.get(id=request.user.pk)
    serializer = UserSerializer(user, many=False)
    if serializer.is_valid():
        serializer.save()
    else:
        Response('There was an error with your update.')
    return Response(serializer.data)

@login_required(login_url='login')
@api_view(['GET'])
def userDetail(request):
    user = User.objects.get(id=request.user.pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@login_required(login_url='login')
@api_view(['DELETE'])
def userDelete(request):
    user = User.objects.get(id=request.user.pk)
    user.delete()
    return Response('This user has been deleted.')