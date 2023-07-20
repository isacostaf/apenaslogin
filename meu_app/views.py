from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

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

def welcome(request):
    return render(request, 'welcome.html')
