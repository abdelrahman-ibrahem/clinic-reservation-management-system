from django import forms 
from .models import Clinic , Appointment

class AddClinic(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = '__all__'


class CreateAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['status' ,'day' , 'time']