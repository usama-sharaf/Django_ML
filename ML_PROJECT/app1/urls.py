
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/',views.welcome, name='welcome'),
    path('aboutMe/',views.aboutme, name='aboutMe'),
    path('userINPUT/',views.userINPUT, name='userINPUT'),

    path('',views.login_view, name='login'),
    path('signup/',views.signup_view, name='signup'),


]