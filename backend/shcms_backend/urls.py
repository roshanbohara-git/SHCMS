"""
URL configuration for shcms_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from api.views import register_doctor, register_patient, landing_page,login_page,doctor_profile_view,patient_profile_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', landing_page, name='landing'),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('login/', login_page, name='html-login'),
    path('register/doctor/', register_doctor, name='register-doctor'),
    path('register/patient/', register_patient, name='register-patient'),
    path('profile/doctor/', doctor_profile_view, name='doctor-profile'),
    path('profile/patient/', patient_profile_view, name='patient-profile'),
    path('logout/', LogoutView.as_view(next_page='html-login'), name='logout'),
]
