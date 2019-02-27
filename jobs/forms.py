from django import forms

from .models import ContactUser

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactUser
        fields = [
            'user',
            'email',
            'content'
        ]