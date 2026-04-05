from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name='add'),
    path('show/', views.show_student, name='show'),

    path('edit/<int:id>/', views.edit_student, name='edit'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
]