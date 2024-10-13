from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Create your views here.
def login(request):
    if request.method == "POSt":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): # 인증된 사용자라면 로그인 진행 세션 데이터 생성
            auth_login(request, form.get_user) #인증된 유저 객체를 넣어야 한다.
            return redirect("articles:index")

    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect("articles:index")

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request, "accounts/signup.html", context)

def delete(request):
    request.user.delete()
    return redirect("articles:index")

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form': form
    }
    return render(request, "accounts/update.html", context)

def change_password(request, user_pk):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.data)
        if form.is_valid():
            form.save()
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request, "accounts/change_password.html", context)