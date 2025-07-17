from django.shortcuts import render, redirect, get_object_or_404
from .models import Cheque, Project, Employee
from .forms import ChequeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

@login_required
def cheque_dashboard(request):
    cheques = Cheque.objects.all().order_by('-created_at')
    projects = Project.objects.all()
    return render(request, 'cheque_dashboard.html', {'cheques': cheques, 'projects': projects})

@login_required
def add_cheque(request):
    if request.method == 'POST':
        form = ChequeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cheque_dashboard')
    else:
        form = ChequeForm()
    return render(request, 'add_cheque.html', {'form': form})

@login_required
def cheque_detail(request, cheque_id):
    cheque = get_object_or_404(Cheque, id=cheque_id)
    return render(request, 'cheque_detail.html', {'cheque': cheque})

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('cheque_dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cheque_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            # Don't redirect, just show the error on the same page
            return render(request, 'login.html')
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    return redirect('login')
