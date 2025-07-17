# urls.py
from django.urls import path
from .views import cheque_dashboard, add_cheque, cheque_detail

urlpatterns = [
    path('', cheque_dashboard, name='cheque_dashboard'),
    path('add/', add_cheque, name='add_cheque'),
    path('cheque/<int:cheque_id>/', cheque_detail, name='cheque_detail'),
]
