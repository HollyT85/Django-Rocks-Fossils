from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_rocks, name="rocks"),
    path('just_rocks', views.just_rocks, name="just_rocks"),
    path('just_fossils', views.just_rocks, name="just_fossils"),

    path('int:<rock_id>', views.rock_info, name='rock_info'),
    path('add/', views.add_rock, name='add_rock'),
    path('edit/<int:rock_id>/', views.edit_rock, name='edit_rock'),
]