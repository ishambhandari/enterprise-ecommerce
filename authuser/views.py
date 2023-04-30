from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login,logout
from .models import User
from django.contrib.auth.hashers import make_password
from .forms import CustomUserCreationForm
# Create your views here.

class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data.get('password'))
        return super().form_valid(form)



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')  # Redirect to the home page after successful login
        else:
            print("erroe")
            error_msg = 'Invalid login credentials. Please try again.'
            return render(request, 'login.html', {'error_msg': error_msg})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def login_page(request):
    return render(request, "login.html")

