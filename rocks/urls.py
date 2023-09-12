from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_rocks, name="rocks"),
    path('int:<rock_id>', views.rock_info, name='rock_info')
    # path('add/', views.add_rock, name='add_rock'),
]