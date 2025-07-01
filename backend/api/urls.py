from django.urls import path,include
from .views import register_doctor, register_patient, login_page, doctor_profile_view,patient_profile_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, user_profile, landing_page

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet, basename='appointment')

urlpatterns = [
    path('', landing_page, name='landing'),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # POST /api/login/
    path('login/', login_page, name='html-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # POST /api/token/refresh/
    path('register/patient/', register_patient, name='register-patient-api'),
    path('register/doctor/', register_doctor, name='register-doctor-api'),
    path('profile/doctor/', doctor_profile_view, name='doctor-profile'),
    path('profile/patient/', patient_profile_view, name='patient-profile'),
]
urlpatterns += router.urls
