from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateUserForm

def UserLoginRegister(request):
    if request.user.is_authenticated:
        return redirect('Chatty:index')
    else:
        if request.method != 'POST':        
            form = CreateUserForm()
        else:
            if 'Sign-up' in request.POST:
                form = CreateUserForm(data=request.POST)
                if form.is_valid():
                    form.save()     
                    userSignUp = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created for ' + userSignUp)               

            elif 'Login' in request.POST:
                username = request.POST.get('user_signin')
                password = request.POST.get('pwd_signin')
                user = authenticate(request,username=username,password=password)

                if user is not None:
                    login(request, user)
                    return redirect('Chatty:index')
                else:
                    messages.info(request, 'Username or password is incorrect!')
                    return redirect('Chatty:user')   

        context = {'form':form}
        return render(request,'User.html',context)    

@login_required(login_url='Chatty:user')
def index(request):
    return render(request, 'home.html')

def logoutUser(request):
    logout(request)
    return redirect('Chatty:user')