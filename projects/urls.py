from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    # map detail to url with project number variable
    path("<int:pk>/", views.project_detail, name="project_detail"),
]