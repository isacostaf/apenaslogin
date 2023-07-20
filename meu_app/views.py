from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django.contrib.auth.decorators import login_required

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
