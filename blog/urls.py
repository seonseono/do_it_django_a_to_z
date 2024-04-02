from django.urls import path
from . import views
# 해당 경로 안의 views를 import

urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]