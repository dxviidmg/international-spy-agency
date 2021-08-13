from django.urls import path
#from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('hitman/<int:pk>/', views.HitmanUpdateView.as_view(), name='hitman-update'),
    path('hitmen/', views.HitmenListView.as_view(), name='hitmen-list'),
    
]
