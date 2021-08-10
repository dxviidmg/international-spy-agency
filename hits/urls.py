from django.urls import path
from . import views


urlpatterns = [
    path('hits/', views.HitListView.as_view(), name='hit-list'),
]