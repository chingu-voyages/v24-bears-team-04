from django.urls import path
from . import views
from .views import (
    CandidateListView
)

urlpatterns = [
    path('candidates', CandidateListView.as_view(), name='candidate-list'),
    path('vote/', views.vote, name='vote'), 
]