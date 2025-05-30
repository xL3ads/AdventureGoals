from django.urls import path
from Userextend import views
urlpatterns = [
    path('create_user/', views.UserCreateView.as_view(), name='create-user' ),
    path('user_login/', views.UserLoginView.as_view(), name='user-login' ),
]