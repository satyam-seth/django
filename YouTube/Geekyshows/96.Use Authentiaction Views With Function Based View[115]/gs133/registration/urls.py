from django.urls import path,include
from registration import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]
