from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('retrive_from_db/', views.retrive_from_db),
    path('fetch_and_save/', views.fetch_and_save),
]

