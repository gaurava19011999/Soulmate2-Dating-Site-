from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models 


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """Creating a user with email is succesful"""
        email = 'test@abc.com'
        password = 'password123'
        user = get_user_model().objects.create_user(
            email =email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    def test_new_user_email_normalized(self):
        """Test the new email for user is normalized"""
        email = 'test@ABC.cOm'
        user = get_user_model().objects.create_user(email, 'password124')

        self.assertEqual(user.email, email.lower()) 

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'passswer124')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        email = 'test@abc.com'
        password = 'pasafnak123'
        user = get_user_model().objects.create_superuser(
            email = email,
            password = password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
