from django.urls import path
from . import views
from .views import test_static

urlpatterns = [
    path('movies/', views.movies, name='movies'),
    path('test-static/', test_static),
]