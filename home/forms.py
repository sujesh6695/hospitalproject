from django import forms
from . models import booking
class dateinput(forms.DateInput):
    input_type='date'
class bookingForm(forms.ModelForm):
    class Meta:
        model=booking
        fields = '__all__'

        widgets= {
            'booking_date' : dateinput()
        }

        labels= {
            'p_name' :  "patient name:",
             'p_phone':  "patient phone:",
             'p_email' :  "patient email:",
             'doc_name' : "doctors name:",
             'booking_date' : "booking date:",
             
        }