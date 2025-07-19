# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cheque_dashboard, name='cheque_dashboard'),
    path('add/', views.add_cheque, name='add_cheque'),
    path('cheque/<int:cheque_id>/', views.cheque_detail, name='cheque_detail'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('cheques/<int:cheque_id>/edit/', views.edit_cheque, name='edit_cheque'),
    path('cheques/<int:cheque_id>/delete/', views.delete_cheque, name='delete_cheque'),
]
