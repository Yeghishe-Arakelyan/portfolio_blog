from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('search/', views.search, name='search'),

]
