from django.shortcuts import render
from .models import Clinic , Appointment , Reservation
from .serializers import AppointmentApi , ClinicApi
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.views.generic import ListView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin # for check if the user is logged in or not
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# for template view

class GetAllClinic(ListView):
    model = Clinic
    context_object_name = 'clinics'
    template_name = 'clinic.html'



class GetSignleClinic(DetailView):
    model = Clinic
    context_object_name = 'clinic'
    template_name = 'clinic_detail.html'

class GetAllAppointments(ListView):
    model = Clinic
    context_object_name = 'appointments'
    template_name = 'clinic_detail.html'

@login_required
def reservation(request , appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        '''
            get the appointment id
            get the user if the user is logged in 
            create reservation 
        '''
        if request.method == 'post':
            user = request.user
            make_reservation = Reservation.objects.create(appointment=appointment , user=user)
            return redirect('') # the same page
    except:
        return redirect('home')



# for apis
class GetAllClinicApi(APIView):
    def get(self , request , *args , **kwargs):
        try:
            response = Clinic.objects.all()
            count = response.count()
            serializers = ClinicApi(response , many=True)
            if count > 0:
                return Response({
                    "message": 'no clinic'
                })
            else: 
                return Response(serializers.data)
        except:
            return Response({
                    "message": 'Error'
                })



class GetSingleClinicApi(APIView):
    def get(self , request , clinic_id , *args , **kwargs):
        try:
            response = Clinic.objects.get(id=clinic_id)
            serializers = ClinicApi(response)
            return Response(serializers.data)
        except:
            return Response({
                    "message": 'Error'
                })

class GetAllAppointment(APIView):
    def get(self , request , *args , **kwargs):
        try:
            response = Appointment.objects.all()
            count = response.count()
            serializers = AppointmentApi(response , many=True)
            if count > 0:
                return Response({
                    "message": 'no Appointments'
                })
            else: 
                return Response(serializers.data)
        except:
            return Response({
                    "message": 'Error'
                })

class MakeAppointment(APIView):
    pass


class DeleteAppointment(APIView):
    pass