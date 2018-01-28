# sendemail/forms.py
from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['email', 'subject', 'message']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(
                attrs={'placeholder': 'Message'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
        }