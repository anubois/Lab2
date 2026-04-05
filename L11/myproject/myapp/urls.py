from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name='add'),
    path('show/', views.show_student, name='show'),
]