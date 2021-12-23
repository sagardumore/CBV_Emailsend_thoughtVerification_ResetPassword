from django.shortcuts import render,redirect
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import random

otp = None
user = None
def registerView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            global user
            username = request.POST['username']
            email = request.POST['email']
            form.save()
            user = User.objects.get(username=username)
            user.is_active = False
            user.save()
            global otp
            otp = random.randint(10000,99999)
            subject = 'verification otp'
            message = f'Hi {username}, thank you for registering in Python Stackflow.Your email verification OTP is {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect("otp_verify")
    template_name = 'TokenApp/register.html'
    context = {'form':form}
    return render(request, template_name, context)

def loginView(request):
    if request.method == 'POST':
        u = request.POST.get("un")
        p = request.POST.get("pw")
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect("show_laptop")
        else:
            messages.error(request,"Invalid username or password")
    template_name = 'TokenApp/login.html'
    context = {}
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect("login")

def otpVerifyView(request):
    if request.method == 'POST':
        num = request.POST.get('otp')
        if int(num) == otp:
            user.is_active = True
            user.save()
            return redirect("login")
        else:
            messages.error(request,"Invalid otp")
    template_name = 'TokenApp/otpverify.html'
    context = {}
    return render(request, template_name, context)