from django.db import models


class Appointment(models.Model):
    doctor_name = models.CharField(max_length=255)
    patient_name = models.CharField(max_length=255)
    patient_email = models.EmailField()
    patient_phone = models.CharField(max_length=20, blank=True, null=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.patient_name}..." # Notice the typo 'paient_name'

    
