from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Bookapoinment(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    symptoms = models.CharField(max_length=250)
    choose_date_1 = models.DateField()

    def __str__(self):
        return f'{self.patient_name}'
    

class PatientDetail(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    PAYMENT_CHOICES = [
        ('C', 'Completed'),
        ('P', 'Pending'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    address = models.TextField()
    patient_disease = models.TextField()
    admission_date = models.DateField()
    discharge_date = models.DateField()
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES)

    def __str__(self):
        return f'{self.first_name}'
