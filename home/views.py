from django.http import HttpResponse
from django.shortcuts import render
from . models import departments,doctors
from . forms import bookingForm
# Create your views here.
def index(request):
  return render(request, "index.html")
def about(request):
  return render(request, "about.html")

def booking(request):
   if request.method=="POST":
     form=bookingForm(request.POST)
     if form.is_valid():
       form.save()
       return render(request,'confirmation.html')
   
   form=bookingForm()
   dict_form={
     'form':form
   }
   return render(request, "booking.html",dict_form)

def doctor(request):
  dict_docs ={
    'doct': doctors.objects.all()
  }
  return render(request, "doctors.html", dict_docs)

def contact(request):
  return render(request, "contact.html")
def department(request):

  dict_dept={
     'dept': departments.objects.all()
  }
  
  return render(request, "department.html", dict_dept)