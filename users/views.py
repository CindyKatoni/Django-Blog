from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now Login')
            return redirect('login')
    else:
        form = UserRegisterForm()   
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)