from django.urls import path 
from .views import *

urlpatterns = [
    path('api/' , GetAllClinicApi.as_view() , name="all_clinic_api"),
    path('api/<int:clinic_id>' , GetSingleClinicApi.as_view() ,name="single_clinic_api"),
    path('api/create' , MakeAppointment.as_view() , name="make_appointment"),
]