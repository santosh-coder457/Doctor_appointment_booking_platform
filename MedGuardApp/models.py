from django.db import models


DOCTOR_CHOICES = [
    ('Dr.E.Shilpa Ghosh', 'Dr.E.Shilpa Ghosh, Gynecology'),
    ('Dr.S.Bhawna Sirohi', 'Dr.S.Bhawna Sirohi,Medical Oncology'),
    ('Dr.H.Ravinder Gera', 'Dr.H.Ravinder Gera,ENT'),
    ('Dr.Jeeson C Unni', 'Dr.Jeeson C Unni,Paediatrics'),
    ('Dr.R.Aswathy.', 'Dr.R.Aswathy,Anaesthesiology & Critical Care'),
    ('Dr.M.Aravind', 'Dr.M.Aravind, Liver Transplant Surgery'),
    ('Dr. T.Sai Kishore', 'Dr. T.Sai Kishore,Neurology'),
    ('Dr.V.Randhir Sud', 'Dr.V.Randhir Sud,Gastroenterology'),
    ('Dr.S.Vinod Raina', 'Dr.S.Vinod Raina,Medical Oncology'),
    ('Dr.A.Naresh Trehan', 'Dr.A.Naresh Trehan,Cardiology'),
    ('Dr.M.Manikandan', 'Dr.M.Manikandan,Hematology'),
    ('Dr.P.Asha Kishore', 'Dr.P.Asha Kishore,Neurology'),
    
]


class Appointment(models.Model):
    doctor_name = models.CharField(max_length=255,choices=DOCTOR_CHOICES,)
    patient_name = models.CharField(max_length=255)
    patient_email = models.EmailField()
    patient_phone = models.CharField(max_length=20, blank=True, null=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.patient_name}..." # Notice the typo 'paient_name'

    

    
