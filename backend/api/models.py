from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')

    def __str__(self):
        return f"{self.username} ({self.role})"
# models.py

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    first_name = models.CharField(max_length = 255, default = 'First')
    middle_name = models.CharField(max_length = 255, blank = True, default = '')
    last_name = models.CharField(max_length = 255, default = 'Last') 
    specialization = models.CharField(max_length=100,default = 'General')
    contact_number = models.CharField(max_length=20, default = '0000000000')
    email = models.EmailField(default = 'doctor1@example.com')
    
    # def __str__(self):
    #     return self.user.username

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    first_name = models.CharField(max_length = 255, default = 'First')
    middle_name = models.CharField(max_length = 255, blank = True, default = '')
    last_name = models.CharField(max_length = 255, default = 'Last')
    dob = models.DateField(default = '2000-01-01')
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=20,default = '0000000000')
    email = models.EmailField(default = 'patient@example.com')
    address = models.TextField(default='Unknown')
    # registration_date = models.DateField()
    blood_group = models.CharField(max_length=10, default = ' Unknown')
    emergency_contact = models.CharField(max_length=20, default = '0000000000')

    # def __str__(self):
    #     return self.user.username
    # other fields...

class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments_as_doctor')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments_as_patient')
    date = models.DateTimeField()
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Appointment on {self.date} between Dr. {self.doctor.username} and {self.patient.username}"

