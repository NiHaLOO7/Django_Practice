from django.urls import path, re_path
from basic_app import views

# Template tagging
app_name = 'basic_app'

urlpatterns = [
    re_path(r'^$', views.index, name='Index'),
    path('relative/', views.relative, name='Relative'),
    path('other/', views.other, name='Others')
]

