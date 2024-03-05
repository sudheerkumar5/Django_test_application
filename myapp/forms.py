# myapp/forms.py
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    mobile_number = forms.CharField(max_length=15)

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6)
