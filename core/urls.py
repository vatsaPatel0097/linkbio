from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add-link/", views.add_link, name="add_link"),
    path("delete-link/<int:link_id>/", views.delete_link, name="delete_link"),

    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("<str:username>/", views.public_profile, name="public_profile"),
]