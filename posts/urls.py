from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name="posts"),
    path('int:<post_id>', views.post_info, name='post_info')
    # path('add/', views.add_post, name='add_post'),
]