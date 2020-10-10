from django.urls import path, include
from . import views

app_name='instagram'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail),
]
