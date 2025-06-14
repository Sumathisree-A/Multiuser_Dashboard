from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    user_type = forms.ChoiceField(choices=Profile.USER_TYPES)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    address_line1 = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    pincode = forms.CharField()
    profile_picture = forms.ImageField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get("password")
        confirm_pwd = cleaned_data.get("confirm_password")
        if pwd and confirm_pwd and pwd != confirm_pwd:
            self.add_error('confirm_password', "Passwords do not match.")
