from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume_view', views.resume_view, name='resume_view'),
    path('projects', views.projetcs, name='projects'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('error', views.error404, name='error'),
]
