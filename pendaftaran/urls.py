from django.urls import path
from . import views
from cek_data.views import cek_data

urlpatterns = [
    path("", views.index, name="index"),
    path("konfirmasi-sukses", views.konfirmasi, name="konfirmasi"),
    path("cek-data", cek_data, name="cek-data"),
]
