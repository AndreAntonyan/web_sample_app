from django.urls import path
from . import views

# import path and views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about')
]