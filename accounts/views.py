from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy



def signupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = CustomUser.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form':form})

def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:allProdCat')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request,'signin.html', {'form':form })

def signoutView(request):
    logout(request)
    return redirect('signin')

class updateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    success_url = reverse_lazy('profile')

class deleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('signup')

def profileView(request):
    return render(request,'profile.html')
