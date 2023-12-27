from django.shortcuts import render,redirect
from .forms import CreateUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def home(request):
    return render(request, 'account/home.html')



def register(request):
    if request.user.is_authenticated :
        return redirect('home')
    else:
        form = CreateUser()
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid:
                form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                messages.success(request, "Account was Created for " + username)
                subject = 'welcome to My Project'
                message = f'Hi {username}, thank you for registering in My Project.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email,]
                send_mail( subject, message, email_from, recipient_list )
                messages.success(request, "We have Email to " + username)
                return redirect('signin')
        
        dictionary = {
            "form":form
        }
        return render(request, 'account/register.html', dictionary)




def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username =  request.POST.get('username')
            password =  request.POST.get('password')
            user  = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Incorrect Password or Username')

        return render(request, 'account/signin.html')



@login_required(login_url='signin')
def signout(request):
    logout(request)
    return render(request, 'account/signout.html')

