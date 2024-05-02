from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.views import View
from users.models import User
from profiles.models import UserProfile
from .forms import LoginForm, RegistrationForm



class Logout(View):
    
    def get(self, request):
        
        logout(request)
        
        return redirect('/')



class Login(View):
    
    def get(self, request):
        
        form = LoginForm()
        
        return render(
            request, 'authentication/login.html', {
                'form' : form
            }
        )
    
    
    def post(self, request):
        
        if request.user.is_authenticated == False:
            
            form = LoginForm(request.POST)
            
            if form.is_valid():
                
                cd = form.cleaned_data
                
                user = authenticate(
                    username=cd['email'],
                    password=cd['password']
                )
                
                if user is not None:
                    
                    login(request, user)
                    
                    return redirect('/')
                else:
                    return render(
                        request, 'authentication/login.html', {
                            'form' : form
                        }
                    )
            else:
                return redirect('authentication:login')
        else:
            return redirect('/')



class Register(View):
    
    def get(self, request):
        
        form = RegistrationForm()
        
        return render(
            request, 'authentication/register.html', {
                'form' : form
            }
        )
        
    
    def post(self, request):
         
        if request.user.is_authenticated == False:
            
            form = RegistrationForm(request.POST)
            
            if form.is_valid():
                
                cd = form.cleaned_data
                
                if cd['password'] == cd['password_conf']:
                    
                    if len(cd['password_conf']) <= 8 and len(cd['password_conf']) >= 8:
                            
                        user = User.objects.create_user(
                            email = cd['email'],
                            username = cd['username'],
                            password = cd['password'],
                        )
                        
                        login(request, user)
                        
                        return redirect('/')
                    else:
                        form.add_error('password_conf', 'رمز عبور وارد شده کوچکتر از ۸ و یا بزرگتر از ۱۶ است')
                else:
                    form.add_error('password_conf', 'رمز عبور خود را اشتباه وارد کردید')   
            else:
                return redirect('authentication:register')
        else:
            return redirect('/')