from django.urls import path
from .views import ProfileView, SkillsView

urlpatterns = [
    path("", ProfileView.as_view()),
    path("skills/", SkillsView.as_view()),
]