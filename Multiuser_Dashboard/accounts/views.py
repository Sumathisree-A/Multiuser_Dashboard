from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, 'accounts/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(
                user=user,
                user_type=form.cleaned_data['user_type'],
                profile_picture=form.cleaned_data['profile_picture'],
                address_line1=form.cleaned_data['address_line1'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode']
            )
            messages.success(request, 'Signup successful! Please login.')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if hasattr(user, 'profile'):
                if user.profile.user_type == 'doctor':
                    return redirect('doctor_dashboard')
                else:
                    return redirect('patient_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout

@login_required
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html')

@login_required
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html')
