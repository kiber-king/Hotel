from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(),
    ),
    path('signup/', views.SignUp.as_view()),
    path('login/',
         LoginView.as_view()),
]
