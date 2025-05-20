from django.shortcuts import render,redirect
from .forms import AppointmentForm
from .models import *

def dashpage(request):

    return render (request,'dashboard.html')

def find_doctors(request):

    return render(request,'find_doctor.html')

def consult(request):

    return render(request,'consult_online.html')

def medical(request):

    return render (request,'medicine.html')

def lab(request):

    return render(request,'laps.html')

def surgrey(request):

    return render(request,'Surgeries.html')

def tip(request):

    return render(request,'tips.html')

def more(request):

    return render(request,'more_guard.html')

def logsing(request):

    return render(request,'login-signup.html')

def appointment(request):

    return render(request,'appointment.html')

def about(request):

    return render(request,'More details/about_us.html')

def contact(request):

    return render(request, 'More details/contact-us.html')

def careers(request):

    return render(request,'More details/careers.html')

def faqs(request):

    return render(request,'More details/FAQ.html')

def privacy(request):

    return render(request,'More details/privacy.html')

def term(request):

    return render(request,'More details/terms.html')

def apply(request):

    return render(request,'More details/apply-career.html')

# doctors_about

def drsai(request):

    return render(request,'doctors about/dr-tsai-kishore.html')

def drnaresh(request):

    return render(request,'doctors about/drnaresh-trehan.html')

def shilpa(request):

    return render(request,'doctors about/dreshilpa-ghosh.html')

def ravinder(request):

    return render(request,'doctors about/drhravinder-gera.html')

def jeeson(request):

    return render(request,'doctors about/drjeeson-c-unni.html')

def aravind(request):

    return render(request,'doctors about/drmaravind.html')

def mani(request):

    return render(request,'doctors about/drmmanikandan.html')

def asha(request):

    return render(request,'doctors about/drpasha-kishore.html')

def aswathy(request):

    return render(request,'doctors about/drraswathy.html')

def bhawna(request):

    return render(request,'doctors about/drsbhawna-sirohi.html')

def vinod(request):

    return render(request,'doctors about/drsvinod-raina.html')

def randhir(request):

    return render(request,'doctors about/drvrandhir-sud.html')


def appointment(request):

    context = {

        "appointment_form" : AppointmentForm
    }

    if request.method == "POST":

        appointment_form = AppointmentForm(request.POST)

        appointment_form.is_valid()

        appointment_form.save()

    return render(request,'appointment.html',context)



def history(request):

    context = {

        "all_history" : Appointment.objects.all()
    }

    return render (request,'appointment_add.html',context)



def Delete(request,id):

    select_appointment = Appointment.objects.get(id = id)

    select_appointment.delete()

    return redirect ('/MedguardHome/appointment/history')



def Update (request,id):

    select_appointment = Appointment.objects.get(id = id)

    context = {

        'form' : AppointmentForm(instance = select_appointment)

    }

    return render (request , 'appointment.html',context)