from django.contrib import admin
from .models import Tour, Client, Booking

class TourAdmin(admin.ModelAdmin):
    list_display = ('tour_id', 'tour_name', 'duration', 'price')
    list_filter = ('duration', 'price')
    search_fields = ('tour_name', 'description')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'surname', 'first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('surname',)
    search_fields = ('first_name', 'surname', 'last_name', 'email')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'client', 'tour', 'booking_date')
    list_filter = ('booking_date', 'client', 'tour')
    search_fields = ('client__first_name', 'client__surname', 'tour__tour_name')

admin.site.register(Tour, TourAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Booking, BookingAdmin)