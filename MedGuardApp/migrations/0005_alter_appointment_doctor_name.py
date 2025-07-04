# Generated by Django 5.2 on 2025-05-14 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedGuardApp', '0004_remove_appointment_reason_for_appointment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor_name',
            field=models.CharField(choices=[('Dr.E.Shilpa Ghosh', 'Dr.E.Shilpa Ghosh'), ('Dr.S.Bhawna Sirohi', 'Dr.S.Bhawna Sirohi'), ('Dr.H.Ravinder Gera', 'Dr.H.Ravinder Gera'), ('Dr.Jeeson C Unni', 'Dr.Jeeson C Unni'), ('Dr.R.Aswathy.', 'Dr.R.Aswathy.'), ('Dr.M.Aravind', 'Dr.M.Aravind'), ('Dr. T.Sai Kishore', 'Dr. T.Sai Kishore'), ('Dr.V.Randhir Sud', 'Dr.V.Randhir Sud'), ('Dr.S.Vinod Raina', 'Dr.S.Vinod Raina'), ('Dr.A.Naresh Trehan', 'Dr.A.Naresh Trehan'), ('Dr.M.Manikandan', 'Dr.M.Manikandan'), ('Dr.P.Asha Kishore', 'Dr.P.Asha Kishore')], max_length=255),
        ),
    ]
