from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('retrieve_from_db/<str:countryCode_str>/', views.retrieve_from_db),
    path('fetch_and_save/', views.fetch_and_save),
]

