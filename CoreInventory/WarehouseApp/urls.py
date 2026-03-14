from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.warehouse_list, name='warehouse_list'),
    path('add/', views.add_warehouse, name='add_warehouse'),
    path('edit/<int:w_id>/', views.edit_warehouse, name='edit_warehouse'),
    path('delete/<int:w_id>/', views.delete_warehouse, name='delete_warehouse'),
]