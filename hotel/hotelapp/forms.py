from django import forms
from.models import Booking
class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        widgets={
            'checkin_date':DateInput(),
            'checkout_date':DateInput(),
        }
        labels={
            'cus_name':"Cutomer Name:",
            'cus_phone':"Customer Phone",
            'name':"Room name",
            'checkin_date':"Check In Date",
            'checkout_date':"Check Out Date",
        }