from django.urls import path
from products import views

urlpatterns = [
    path('show/', views.display),
    path('add/', views.add)
]