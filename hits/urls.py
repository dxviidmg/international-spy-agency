from django.urls import path
from . import views


app_name = 'hits'

urlpatterns = [
    path('hits/', views.HitListView.as_view(), name='hit-list'),
]