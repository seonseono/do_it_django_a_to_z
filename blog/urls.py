from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
# 해당 경로 안의 views를 import

urlpatterns = [
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
