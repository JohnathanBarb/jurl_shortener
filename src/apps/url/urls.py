from django.urls import path
from src.apps.url import views


urlpatterns = [
    path("", views.CreateUrlView.as_view(), name="create_shortened_url"),
    path("<str:token>/", views.get_shortened_url, name="get_shortened_url"),
]
