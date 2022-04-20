from rest_framework import serializers
from .models import Clinic , Appointment , Reservation


class ClinicApi(serializers.ModelSerializer):
    class Meta:
        model = Clinic 
        fields = ['name' , 'telephone' , 'address' , 'email']



class AppointmentApi(serializers.ModelSerializer):
    class Meta:
        model = Appointment 
        fields = ['status' , 'date' , 'time']
