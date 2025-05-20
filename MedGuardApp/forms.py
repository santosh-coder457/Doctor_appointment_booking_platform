# from django import forms
# from .models import Appointment, DOCTOR_CHOICES

# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = '__all__'

from django import forms
from .models import Appointment # Make sure your Appointment model is imported

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'doctor_name',
            'patient_name',
            'patient_email',
            'patient_phone',
            'appointment_date',
            'appointment_time',
            'reason'
        ]
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),

            'reason': forms.Textarea(attrs={'rows': 4}),
        }