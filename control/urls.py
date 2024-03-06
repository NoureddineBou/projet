from django.urls import path
from . import views

urlpatterns = [
  path('clients/create.html/', views.create, name='createe'),
  path('clients/view_profile.html/', views.view_profile, name='profile'),
  path('clients/login.html/', views.loginn, name='loginn'),
  path('', views.home, name= 'home'),
  # path('logout', views.signout, name='signout'),

]
