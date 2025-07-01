from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .serializers import RegisterSerializer, UserProfileSerializer, AppointmentSerializer
from .forms import RegisterForm, DoctorProfileForm, PatientProfileForm
from .models import Appointment
# from django.views.decorators.csrf import csrf_exempt

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    if request.method == 'GET':
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @csrf_exempt
def register_doctor(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        doctor_form = DoctorProfileForm(request.POST)
        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save(commit=False)
            user.role = 'doctor'
            user.save()
            doctor_profile = doctor_form.save(commit=False)
            doctor_profile.user = user
            doctor_profile.save()
            return redirect('html-login')
    else:
        user_form = RegisterForm()
        doctor_form = DoctorProfileForm()

    return render(request, 'register_doctor.html', {
        'user_form': user_form,
        'doctor_form': doctor_form
    })

def register_patient(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        patient_form = PatientProfileForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save(commit=False)
            user.role = 'patient'
            user.save()
            patient_profile = patient_form.save(commit=False)
            patient_profile.user = user
            patient_profile.save()
            return redirect('html-login')
    else:
        user_form = RegisterForm()
        patient_form = PatientProfileForm()

    return render(request, 'register_patient.html', {
        'user_form': user_form,
        'patient_form': patient_form
    })
@login_required
def doctor_profile_view(request):
    return render(request, 'doctor_profile.html')

@login_required
def patient_profile_view(request):
    return render(request, 'patient_profile.html')

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.role == 'doctor':
                return redirect('doctor-profile')
            elif user.role == 'patient':
                return redirect('patient-profile')
            elif user.role == 'admin':
                return redirect('/admin/')
            return redirect('/')  # fallback
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


class AppointmentViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Appointment.objects.all()
        elif user.role == 'doctor':
            return Appointment.objects.filter(doctor=user)
        elif user.role == 'patient':
            return Appointment.objects.filter(patient=user)
        return Appointment.objects.none()

def landing_page(request):
    return render(request, 'landing.html')
from django.contrib.auth.decorators import login_required


