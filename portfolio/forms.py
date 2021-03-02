from django import forms
from .models import Visitor
from phonenumber_field.formfields import PhoneNumberField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from .tasks import send_contact_message_task

class VisitorContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Full Name',
        }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phone Number',
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address',
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'rows': 7,
    }))

    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = Visitor
        fields = '__all__'

    def send_email(self):
        send_contact_message_task.delay(
            self.cleaned_data['full_name'], 
            self.cleaned_data['email'], 
            self.cleaned_data['phone_number'], 
            self.cleaned_data['message']
        )
        