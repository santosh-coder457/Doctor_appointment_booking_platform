from django import forms
from .models import Appointment, DOCTOR_CHOICES

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'