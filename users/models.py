from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

class User(AbstractUser):
    # use the username for now
    username = models.CharField(max_length=50, verbose_name='username', unique=True, default='user')
    email = models.EmailField(_('email address'), unique=True)

    REQUIRED_FIELDS = ['password', 'email', 'first_name', 'last_name']

    city = models.CharField(max_length=50)

    # ask user to input state code e.g. CA for california, GA for georgia
    state = models.CharField(max_length=3)
    street_address = models.CharField(max_length=50)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True) # validators should be a list
    
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        # reverse takes view name as first arg 
        return reverse('user_dashboard', kwargs={ 'username': self.username })