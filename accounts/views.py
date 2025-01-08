# views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import CustomUserEditForm, CustomUserRegistrationForm,CustomUserLoginForm

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test


from django.contrib.auth.views import LoginView
from .models import CustomUser



def admin_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: user.is_staff,
        login_url='login',  # Redirect to login page if the user is not logged in
        redirect_field_name=None
    )(view_func)
    
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You do not have permission to access this page.")
        return decorated_view_func(request, *args, **kwargs)
    
    return _wrapped_view


def home_view(request):
    return render(request, 'accounts/index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('home')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'There was an error with your registration.')

    else:
        form = CustomUserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # Custom template for login

    def form_valid(self, form):
        # Customize success message or behavior
        messages.success(self.request, 'Welcome back!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Customize error message or behavior
        messages.error(self.request, 'Invalid credentials, please try again.')
        return super().form_invalid(form)
    


@login_required
def profile(request):
    user = request.user  # The logged-in user
    return render(request, 'accounts/profile.html', {'user': user})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('home')  # Redirect to the home page after logout


@admin_required
def admin_dashboard(request):
    users = CustomUser.objects.all()  # Fetch all registered users
    return render(request, 'accounts/dashboard.html', {'users': users})


@admin_required
def admin_user_edit(request, id):
    user = get_object_or_404(CustomUser, id=id)
    
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User details updated successfully!')
            return redirect('dashboard')  # Redirect to the dashboard after saving
        else:
            messages.error(request, 'There was an error updating the user.')
    else:
        form = CustomUserEditForm(instance=user)
    
    return render(request, 'accounts/admin_user_edit.html', {'form': form, 'user': user})