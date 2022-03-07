
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students',views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

"""
urlpatterns = [
    path('students/', views.StudentList.as_view(), name='list'),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name='detail'),
]
"""