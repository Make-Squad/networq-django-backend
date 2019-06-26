from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=25, required=True)
    last_name = models.CharField(max_length=25, required=True)

    email = models.EmailField(min_length=4, required=True)
    
    city = models.CharField(min_length=2, max_length=50)
    # ask user to input state code e.g. CA for california, GA for georgia
    state = models.CharField(max_length=3)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, required=True) # validators should be a list
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)