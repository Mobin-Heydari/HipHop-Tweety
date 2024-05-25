from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.urls import reverse
from django.views import View

from users.models import User

from .forms import LoginForm, RegistrationForm, OtpForm, CahngePasswordForm
from .models import Otp, ResetPasswordOtp

from random import randint



class Logout(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
                
            logout(request)
            
            return redirect('/')
        else:
            return redirect('home:home')



class Login(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == False:
            
            form = LoginForm()

            return render(
                request, 'authentication/login.html', {
                    'form' : form
                }
            )
        else:
            return redirect('home:home')
        
        
    
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
                    
                    return redirect('home:home')
                else:
                    return render(
                        request, 'authentication/login.html', {
                            'form' : form
                        }
                    )
            else:
                return redirect('authentication:login')
        else:
            return redirect('home:home')



class Register(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == False:
            
            form = RegistrationForm()
            
            return render(
                request, 'authentication/register.html', {
                    'form' : form
                }
            )
        else:
            return redirect('home:home')
        
    
    def post(self, request):
         
        if request.user.is_authenticated == False:
            
            form = RegistrationForm(request.POST)
            
            if form.is_valid():
                
                cd = form.cleaned_data
                
                if cd['password'] == cd['password_conf']:
                    
                    if len(cd['password_conf']) <= 8 and len(cd['password_conf']) >= 8:
                        
                        otp_code = randint(100000, 999999)
                        
                        token = get_random_string(100)
                        
                        otp = Otp.objects.create(
                            email = cd['email'],
                            username = cd['username'],
                            password = cd['password'],
                            otp_code = otp_code,
                            token = token
                        )
                        
                        send_mail(
                            subject = 'Hip Hop Tweety veryfication',
                            message = f'به Hip Hop Tweety خوش آمدید. برای تایید ایمیل خودتون کد: {otp_code} را وارد کنید',
                            from_email = 'email@hip-hop-tweety.com',
                            recipient_list = [cd['email']],
                            fail_silently = False,
                        )
                        
                        return redirect(reverse('authentication:check_otp') + f'?token={token}')
                    else:
                        return redirect('authentication:register')
                else:
                    return redirect('authentication:register')
            else:
                return redirect('authentication:register')
        else:
            return redirect('home:home')
        
        
class CheckOtp(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == False:
            
            form = OtpForm()
        
            return render(
                request, 'authentication/check_otp.html', {
                    'form' : form
                }
            )
        else:
            return redirect('home:home')
        
    
    def post(self, request):
        
        if request.user.is_authenticated == False:
            
            form = OtpForm(request.POST)

            token = request.GET.get('token')
            
            otp = get_object_or_404(
                Otp, token = token
            )
            
            if form.is_valid():
                
                cd = form.cleaned_data
                
                if int(cd['otp']) == int(otp.otp_code):
                    
                    user = User.objects.create_user(
                        username = otp.username,
                        password = otp.password,
                        email = otp.email,
                    )
                    
                    user.save()
                    
                    otp.delete()
                    
                    login(request, user)
                    
                    return redirect('home:home')
                else:
                    return render(
                        request, 'authentication/check_otp.html', {
                        'form' : form,
                        }
                    )
            else:
                return render(
                    request, 'authentication/check_otp.html', {
                        'form' : form,
                    }
                )
        else:
            return redirect('homehome:homehome')
        
        

class ResetPassword(View):
    
    def get(self, request):
        
        return render(
            request, 'authentication/reset_password.html', {
                
            }
        )
        
    
    def post(self, request):
        
        email = request.POST.get('email')
        
        try:
            user = User.objects.get(email = email)
            
            code = randint(100000, 999999)
            
            token = get_random_string(100)
            
            
            otp = ResetPasswordOtp.objects.create(
                email = email,
                otp_code = code,
                token = token
            )
            otp.save()
            
            send_mail(
                subject = 'Hip Hop Tweety ریست کردن رمزعبور',
                message = f'به Hip Hop Tweety خوش آمدید. برای تایید ایمیل خودتون کد: {code} را وارد کنید',
                from_email = 'email@hip-hop-tweety.com',
                recipient_list = [email],
                fail_silently = False,
            )
            
            return redirect(reverse('authentication:validate_otp')+ f'?token={token}')
        except User.DoesNotExist:
            return redirect('authentication:reset_password')
        

class ValidatePasswordOtp(View):
    
    def get(self, request):
        
        token = request.GET.get('token')
        
        try:
            otp = ResetPasswordOtp.objects.get(token=token)
            
            return render(
                request, 'authentication/validate_otp.html', {
                    
                }
            )
        except otp.DoesNotExist:
            return redirect('authentication:reset_password')
        
    
    def post(self, request):
        
        token = request.GET.get('token')
        
        try:
            otp = ResetPasswordOtp.objects.get(token=token)
            
            code = request.POST.get('code')
            
            if int(code) == int(otp.otp_code):
                return redirect(reverse('authentication:change_password')+ f'?token={token}')
            else:
                return redirect('authentication:reset_password')
        except otp.DoesNotExist:
            return redirect('authentication:reset_password')

class ChangePassword(View):
    
    def get(self, request):
        
        form = CahngePasswordForm()
        
        return render(
            request, 'authentication/change_password.html', {
                'form' : form
            }
        )
        
    def post(self, request):
        
        form = CahngePasswordForm(request.POST)
        
        token = request.GET.get('token')
        
        password_otp = get_object_or_404(
            ResetPasswordOtp,
            token = token
        )
        
        if form.is_valid():
            
            cd = form.cleaned_data
            
            if len(cd['password_conf']) <= 8 and len(cd['password_conf']) >= 8:
            
                if cd['password'] == cd['password_conf']:
                    
                    user = User.objects.get(email=password_otp.email)
                
                    if user is not None:
                        
                        user.set_password(cd['password'])
                        
                        user.save()
                        
                        # password_otp.delete()
                        
                        return redirect('home:home')
                    else:
                        return redirect('authentication:reset_password')
                else:
                    return render(
                        request, 'authentication/changepassword.html', {
                            
                        }
                    )
            else:
                return render(
                    request, 'authentication/changepassword.html', {
                        
                    }
                )
        else:
            return redirect('authentication:reset_password')