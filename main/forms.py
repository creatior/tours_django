from django import forms
from .models import Tour, Client, Booking

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['tour_name', 'description', 'duration', 'price']
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['surname', 'first_name', 'last_name', 'email', 'phone_number']
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['client', 'tour', 'booking_date']