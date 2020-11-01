from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('vote/<str:pk>', views.vote, name='vote'),

    path('elections/', views.electionList, name='election-list'),
    path('elections/create/', views.electionCreate, name='election-create'),
    path('elections/detail/<str:pk>/', views.electionDetail, name='election-detail'),
    path('elections/update/<str:pk>/', views.electionUpdate, name='election-update'),
    path('elections/delete/<str:pk>/', views.electionDelete, name='election-delete'),
    path('elections/candidates/<str:pk>/', views.electionCandidateList, name='election-candidate-list'),

    path('candidates/', views.candidateList, name='candidate-list'),
    path('candidates/detail/<str:pk>/', views.candidateDetail, name='candidate-detail'),
    path('candidates/create/', views.candidateCreate, name='candidate-create'),
    path('candidates/update/<str:pk>', views.candidateUpdate, name='candidate-update'),
    path('candidates/delete/<str:pk>', views.candidateDelete, name='candidate-delete'),

    path('users/', views.userList, name='user-list'),
    path('users/update/', views.userUpdate, name='user-update'),
    path('users/detail/', views.userDetail, name='user-detail'),
    path('users/delete/', views.userDelete, name='user-delete'),
]