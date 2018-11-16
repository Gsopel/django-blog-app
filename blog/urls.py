from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog_home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/update', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('about', views.about, name='about'),
]


