from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, DoctorProfile, PatientProfile

class RegisterForm(UserCreationForm):
    # Remove role field because you now set role in views explicitly
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['first_name', 'middle_name', 'last_name', 'specialization', 'contact_number', 'email']

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['first_name', 'middle_name', 'last_name', 'dob', 'gender', 'contact_number', 'email', 'address', 'blood_group', 'emergency_contact']
