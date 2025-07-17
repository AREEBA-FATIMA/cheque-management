from django.contrib import admin
from django import forms
from .models import Project, Employee, Cheque

# -------------------------------
# Custom Form for Cheque (Date Pickers + Project Dropdowns)
# -------------------------------
class ChequeAdminForm(forms.ModelForm):
    class Meta:
        model = Cheque
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'cheque_date': forms.DateInput(attrs={'type': 'date'}),
            'responsible_person_project': forms.Select(),
            'received_by_project': forms.Select(),
        }

# -------------------------------
# Project Admin
# -------------------------------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_head_office']
    list_filter = ['is_head_office']
    search_fields = ['name']

# -------------------------------
# Employee Admin
# -------------------------------
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'project']
    list_filter = ['designation', 'project']
    search_fields = ['name', 'designation']

# -------------------------------
# Cheque Admin
# -------------------------------
@admin.register(Cheque)
class ChequeAdmin(admin.ModelAdmin):
    form = ChequeAdminForm
    list_display = [
        'description', 'cheque_number', 'amount', 'status',
        'project',

        # Responsible Person Info
        'responsible_person_name', 'responsible_person_project',
        'responsible_person_contact', 'responsible_person_cnic',

        # Received By Info
        'received_by_name', 'received_by_project',
        'received_by_contact', 'received_by_cnic',

        'approved_by', 'cheque_date'
    ]
    list_filter = ['status', 'approved_by', 'payment_mode', 'project']
    search_fields = [
        'description', 'cheque_number', 'notes',

        # Responsible Person Search
        'responsible_person_name', 'responsible_person_contact', 'responsible_person_cnic',

        # Received By Search
        'received_by_name', 'received_by_contact', 'received_by_cnic',
    ]
    readonly_fields = ['cheque_number']
    date_hierarchy = 'cheque_date'
