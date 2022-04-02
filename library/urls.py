from django.urls import path, include
from .views import *


urlpatterns = [
    path('latest-books/', view=LatestBooksList.as_view()),
]