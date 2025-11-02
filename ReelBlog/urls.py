from django.urls import path
from . import views

app_name = 'ReelBlog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('category/<str:category_name>/', views.category_posts, name='category_posts'),
     path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]
