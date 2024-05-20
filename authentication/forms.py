from django import forms


class LoginForm(forms.Form):
    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'id' : 'email',
                'type' : 'text'
            }
        )
    )
    
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'id' : 'password',
                'type' : 'password'
            }
        )
    )


class RegistrationForm(forms.Form):
    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'id' : 'email',
                'type' : 'text'
            }
        )
    )
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'id' : 'username',
                'type' : 'text'
            }
        )
    )
    
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'id' : 'password',
                'type' : 'password'
            }
        )
    )
    
    password_conf = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'id' : 'password',
                'type' : 'password'
            }
        )
    )
    
class OtpForm(forms.Form):
    
    otp = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'id' : 'otp',
                'type' : 'text'
            }
        )
    )
    
class CahngePasswordForm(forms.Form):
    
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'id' : 'password',
                'type' : 'text'
            }
        )
    )
    
    password_conf = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'id' : 'password',
                'type' : 'text'
            }
        )
    )