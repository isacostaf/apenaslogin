from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm


def login_or_create_account(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password', '')  # Use get() para evitar o erro MultiValueDictKeyError
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('welcome')
    else:
        form = UserCreationForm()

    return render(request, 'login_or_create_account.html', {'form': form})

@login_required
def welcome(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(user=request.user, title=title, description=description)
        return redirect('welcome')

    tasks = Task.objects.filter(user=request.user)
    return render(request, 'welcome.html', {'tasks': tasks})

@login_required
def remove_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('welcome')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})