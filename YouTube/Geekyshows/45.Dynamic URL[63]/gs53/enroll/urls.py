from django.urls import path
from . import views

urlpatterns=[
    # path('', views.show_details, name='detail'),
    # path('<my_id>/', views.show_details, name='detail'),
    path('<int:my_id>/', views.show_details, name='detail'),
    path('<int:my_id>/<int:my_subid>/', views.show_subdetails, name='subdetail'),
]