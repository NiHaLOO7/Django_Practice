from django.urls import path, re_path
from appTwo import views

urlpatterns = [
    re_path(r'^$',views.users,name='users'),
    path('signup/', views.signup, name='signup'),
]
