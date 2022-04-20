from django.test import TestCase
from .models import Clinic , Appointment , Reservation
from django.contrib.auth import get_user_model


class TestClinic(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username= 'abdo',
            email='abdo@gmail.com',
            password='password'
        )

    def test_clinic_model(self):
        clinic = Clinic.objects.create(
            name="name",
            address='address',
            telephone='0122222222',
            email='abdo@gmail.com'
        )
        self.assertEqual(clinic.name, 'name')
        self.assertEqual(clinic.address, 'address')
        self.assertEqual(clinic.telephone, '0122222222')
        self.assertEqual(clinic.email, 'abdo@gmail.com')
    

    def test_appointment_model(self):
        clinic = Clinic.objects.create(
            name="name",
            address='address',
            telephone='0122222222',
            email='abdo@gmail.com'
        )
        appointment = Appointment.objects.create(
            clinic_id= clinic , 
            status =True,
            day="today",
            time="12 pm"
        )
        self.assertEqual(appointment.clinic_id , clinic)
        self.assertEqual(appointment.day , 'today')
        self.assertEqual(appointment.time , '12 pm')
    
