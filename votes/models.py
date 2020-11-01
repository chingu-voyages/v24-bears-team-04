from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

PARTY_CHOICES = [
    ('ACDP', 'African Christian Democratic Party'),
    ('AIC', 'African Independent Congress'),
    ('ATM', 'African Transformation Movement'),
    ('ALJAMAH', 'Al Jama-ah'),
    ('ANC', 'African National Congress'),
    ('COPE', 'Congress of the People'),
    ('DA', 'Democratic Alliance'),
    ('EFF', 'Economic Freedom Fighters'),
    ('FF+', 'Freedom Front Plus'),
    ('GOOD', 'Good'),
    ('IFP', 'Inkatha Freedom Party'),
    ('NFP', 'National Freedom Party'),
    ('PAC', 'Pan Africanist Congress'),
    ('UDM', 'United Democratic Movement'),
    ('Other', 'Other')
]

GENDER_CHOICES = [
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Other', 'Other'),
]

TIER_CHOICES = [
    ('Local', 'Local'),
    ('Regional', 'Regional'),
    ('National', 'National'),
    ('Other', 'Other')
]

class Election(models.Model):
    title = models.CharField(max_length=250)
    tier = models.CharField(max_length=10, choices=TIER_CHOICES, null=True, blank=False)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return "elections/detail/{}".format(self.pk)

class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(blank=False, unique=True)
    birthdate = models.DateField(null=True, blank=True)
    id_number = models.CharField(max_length=16, blank=True, unique=True)
    constituency = models.CharField(max_length=100, blank=True)
    party = models.CharField(max_length=7, choices=PARTY_CHOICES, default='Other')
    phone = models.CharField(max_length=200, blank=True)
    picture_id = models.ImageField(null=True, blank=True)
    picture_self = models.ImageField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    ethnicity = models.CharField(max_length=100, blank=True)
    is_official = models.BooleanField(default=False)
    elections = models.ManyToManyField(Election, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return "users/profile/{}".format(self.pk)

class Candidate(models.Model):
    elections = models.ManyToManyField(Election)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    picture_self = models.ImageField(null=True, blank=True)
    party = models.CharField(max_length=7, choices=PARTY_CHOICES, default='Other')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    ethnicity = models.CharField(max_length=100, blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)

    def get_absolute_url(self):
        return "candidates/detail/{}".format(self.pk)