# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm , UserChangeForm


class CreateCustomUser(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username' , 'password' , 'email')




class ChangeCustomUser(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username' , 'password' , 'email')