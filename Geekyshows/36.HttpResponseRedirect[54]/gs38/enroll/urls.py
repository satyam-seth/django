from django.urls import path
from enroll import views

urlpatterns=[
    path('registration/',views.showformdata),
    path('success/',views.success),
]