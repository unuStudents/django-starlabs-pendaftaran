from django.urls import path
from . import views

urlpatterns = [
    path("wrong", views.kosong, name="kosong"),
]
