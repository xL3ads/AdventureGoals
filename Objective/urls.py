from Objective.views import ObjectiveCreateView
from django.urls import path
from Objective import views

urlpatterns = [
    path('create_objective/', views.ObjectiveCreateView.as_view(), name='create-objective'),
    path('list_objective/', views.ObjectiveListView.as_view(), name='list-objectives'),
]