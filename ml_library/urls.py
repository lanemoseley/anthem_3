from django.urls import path
from . import views

urlpatterns = [
    path("", views.ml_library_detail, name="ml_library_detail"),
]
