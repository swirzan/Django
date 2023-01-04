from django.urls import path
from . import views
urlpatterns = [
    path("homepage/", views.homepage),
    path("addnew/", views.addnew),
]
