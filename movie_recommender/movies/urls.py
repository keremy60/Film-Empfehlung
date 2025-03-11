from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies, name='movies'),
    path('test_static/', views.test_static, name='test_static'),
]
