from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUser(TestCase):
    def test_user_model(self):
        user = get_user_model().objects.create_user(
            username="abdo" , 
            email="abdo@gmail.com",
            password="password"
        )
        self.assertEqual(user.username , 'abdo')
        self.assertEqual(user.email , 'abdo@gmail.com')