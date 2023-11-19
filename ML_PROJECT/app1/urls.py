
from django.urls import path
from . import views

urlpatterns = [


    path('',views.login_views, name='login'),
    path('signup/',views.signup_view, name='signup'),

    path('welcome/',views.welcome, name='welcome'),
    path('aboutMe/',views.aboutme, name='aboutMe'),
    path('userINPUT/',views.userINPUT, name='userINPUT'),
    path('logout/',views.logout_fun, name='logout'),
    path('img_csv/',views.csv_img_fun, name='img_csv'),


]