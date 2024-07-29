from django.contrib.auth.forms import UserCreationForm
from .models import User, Bookapoinment, PatientDetail
from django import forms

class userCustomForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Conform Password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class BookapoinmentdForm(forms.ModelForm):
    patient_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}))
    doctor_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Doctor Name'}))
    department_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Department Name'}))
    phone_no=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}))
    symptoms=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Symtoms '}))
    choose_date_1 = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
    class Meta:
        model = Bookapoinment
        fields = ['patient_name', 'doctor_name', 'department_name', 'phone_no', 'symptoms', 'choose_date_1']


class PatientDetailForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    PAYMENT_CHOICES = [
        ('C', 'Completed'),
        ('P', 'Pending'),
    ]
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your First Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Last  Name'}))
    father_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Father Name'}))
    mother_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Mother Name'}))
    age=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Age'}))
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email Address'}))
    mobile_no=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Mobile No'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Address'}))
    patient_disease=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Disease'}))
    admission_date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type': 'date'}))
    discharge_date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type': 'date'}))
    payment_status=forms.ChoiceField(choices=PAYMENT_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = PatientDetail
        fields = [
            'first_name', 'last_name', 'father_name', 'mother_name',
            'age', 'gender', 'email', 'mobile_no', 'address', 
            'patient_disease', 'admission_date', 'discharge_date', 'payment_status'
        ]
        
        
