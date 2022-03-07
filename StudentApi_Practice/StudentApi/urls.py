from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='list'),
    path('students/<int:pk>/', views.student_detail, name='detail'),
]