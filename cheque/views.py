from django.shortcuts import render, redirect, get_object_or_404
from .models import Cheque, Project, Employee
from .forms import ChequeForm

def cheque_dashboard(request):
    cheques = Cheque.objects.all().order_by('-created_at')
    projects = Project.objects.all()
    return render(request, 'cheque_dashboard.html', {'cheques': cheques, 'projects': projects})

def add_cheque(request):
    if request.method == 'POST':
        form = ChequeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cheque_dashboard')
    else:
        form = ChequeForm()
    return render(request, 'add_cheque.html', {'form': form})

def cheque_detail(request, cheque_id):
    cheque = get_object_or_404(Cheque, id=cheque_id)
    return render(request, 'cheque_detail.html', {'cheque': cheque})
