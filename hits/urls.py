from django.urls import path
from . import views


app_name = 'hits'

urlpatterns = [
    path('hits/', views.HitListView.as_view(), name='hit-list'),
    path('hit/<int:pk>/', views.HitUpdateView.as_view(), name='hit-update'),
    path('hit/create/', views.HitCreateView.as_view(), name='hit-create')
]