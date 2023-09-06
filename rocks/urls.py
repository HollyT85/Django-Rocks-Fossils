from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_rocks, name="rocks"),
    # path('add/', views.add_rock, name='add_rock'),
]