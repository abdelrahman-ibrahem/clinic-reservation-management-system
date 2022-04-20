# clinic/models.py
from django.db import models
from django.contrib.auth import get_user_model 
from django.urls import reverse
# user model
User = get_user_model()

# create clinc model
class Clinic (models.Model):
    name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('' , args=[self.id])

# create Appointment model
class Appointment(models.Model):
    clinic_id = models.ForeignKey(Clinic , on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.clinic_id.name} {self.day} {self.time} '

# Reservation model
class Reservation(models.Model):
    appointment = models.ForeignKey(Appointment , on_delete=models.CASCADE)
    user = models.ForeignKey(User  , on_delete=models.CASCADE)


    def __str__(self):
        return f' {self.user.username}  {self.appointment.clinic_id.name} '
    