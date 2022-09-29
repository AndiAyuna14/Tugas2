from django.shortcuts import render
from urllib import response
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.forms import TodoForm
from todolist.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    
    context = {
        'list_task': data_task,
        'username':request.user,
        'nama': "Andi Ayuna Rymang",
        'npm': "2106638265",
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def add_new_task(request):
    form = TodoForm(request.POST or None)
    response = {
        'form':form,
        'username':request.user
    }
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('todolist:show_todolist')
    return render(request, "create_task.html", response)            