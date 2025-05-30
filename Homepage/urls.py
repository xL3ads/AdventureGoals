

from django.urls import path
from Homepage import views

urlpatterns = [
    path('', views.HomepageView.as_view(),name='home')
]