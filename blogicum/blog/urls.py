from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('posts/<int:post_id>/', views.post, name='post_detail'),
    path(
        'category/<slug:category_slug>/', views.category, name='category_posts'
    ),
    path('', views.index, name='index'),
]
