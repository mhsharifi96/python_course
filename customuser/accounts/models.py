# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

##############
# """
# AbstractBaseUser vs AbstractUser
# AbstractBaseUser requires a very fine level of control and customization. We essentially
# rewrite Django. This can be helpful, but if we just want a custom user model that can be updated
# with additional fields, the better choice is AbstractUser which subclasses AbstractBaseUser .
# In other words, we write much less code and have less opportunity to mess things up. It’s the
# better choice unless you really know what you’re doing with Django!
# """

# AbstractBaseUser : https://testdriven.io/blog/django-custom-user-model/
# User authentication and permissions : https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
#############

# mean blank and null on model ?
# null is database-related. When a field has null=True it can store a database entry as NULL ,meaning no value.
# blank is validation-related, if blank=True then a form will allow an empty value, whereas if blank=False then a value is required.


class CustomUser(AbstractUser):
    
    age = models.PositiveIntegerField(null=True, blank=True)




