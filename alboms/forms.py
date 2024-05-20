from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'نظر خود را بنویسید',
                'id' : 'comment'
            }
        )
    )
    
class ReplyForm(forms.Form):
    reply = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'پاسخ خود را بنویسید',
                'id' : 'comment'
            }
        )
    )