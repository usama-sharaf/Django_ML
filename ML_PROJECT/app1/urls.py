
from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome, name='welcome'),
    path('aboutMe/',views.aboutme, name='aboutMe'),
    path('userINPUT/',views.userINPUT, name='userINPUT'),

]