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