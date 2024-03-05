from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, OTPForm
from .models import UserProfile
import random


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            mobile_number = form.cleaned_data['mobile_number']

            # Generate and save OTP
            otp = str(random.randint(100000, 999999))
            user_profile, created = UserProfile.objects.get_or_create(
                username=username, mobile_number=mobile_number, defaults={'otp': otp}
            )

            # Send OTP (you need to implement this)
            # Example: send_otp_function(mobile_number, otp)

            return redirect('otp_verification', username=username, mobile_number=mobile_number)
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def otp_verification(request, username, mobile_number):
    user_profile = UserProfile.objects.get(username=username, mobile_number=mobile_number)

    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['otp'] == user_profile.otp:
                # OTP is valid, log in the user
                user = authenticate(request, username=username)
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')
    else:
        form = OTPForm()

    return render(request, 'otp.html', {'form': form, 'username': username, 'mobile_number': mobile_number})


def dashboard(request):
    return render(request, 'dashboard.html')
