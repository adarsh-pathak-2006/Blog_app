from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import blogs


def login_u(request):
    return render(request, 'login.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        
        else:
            return render(request, 'login.html', { 'error':'User not found, try registering yourself first' })
        
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

def register_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        password2=request.POST.get('pass2')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                return render (request, 'register.html', { 'error':'user already exist' })
            user=User.objects.create_user(username=username, password=password2)
            login(request, user)
            return redirect('home')
        
        else:
            return render(request, 'register.html', { 'password_err':'enter the same passwords' })
    return render(request, 'register.html')

@login_required
def home(request):
    blog=blogs.objects.filter(author=request.user)
    return render(request, 'home.html',{ 'blog':blog })

@login_required
def add(request):
    return render(request, 'add_blog.html')

@login_required
def create_blog(request):
    if request.method=="POST":
        blogs.objects.create(
            author=request.user,
            title=request.POST.get('title'),
            content=request.POST.get('content')
        )
        return redirect('home')
    return render(request, 'add_blog.html')

@login_required           
def individual(request, id):
    blog = get_object_or_404(blogs, id=id, author=request.user)
    return render(request, 'individual.html', { 'blog':blog })


def logout_user(request):
    logout(request)
    return redirect('login')


def home_main(request):
    blog=blogs.objects.all()
    return render(request, 'home_main.html', {'blog':blog})

def home_main_individual(request, id):
    blog_indivi=get_object_or_404(blogs,id=id)
    return render(request, 'blog_main_individual.html', { 'blog_ind':blog_indivi })