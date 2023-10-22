from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
# from store.models.customer import Customer
from django.views import View

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Customer
from django.views import View
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.core.mail import send_mail


# Add more custom validation rules as needed
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Welcome {username}, your account is successfully created', )
            return redirect('login')
    else:

        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})








