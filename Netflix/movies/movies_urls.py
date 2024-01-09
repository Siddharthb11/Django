from django.urls import path
from movies import views

urlpatterns = [
    path('home/', views.display),
    path('show/', views.show_movies)
]