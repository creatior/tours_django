from django.shortcuts import render, get_object_or_404, redirect
from .models import Tour, Client, Booking
from .forms import TourForm, ClientForm, BookingForm

def main_page(request):
    return render(request, 'main_page.html')

def tours_list(request):
    tours = Tour.objects.all()
    return render(request, 'tour_list.html', {'tours': tours})

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    return render(request, 'tour_detail.html', {'tour': tour})

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'clients_list.html', {'clients': clients})

def bookings_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings_list.html', {'bookings': bookings})

def add_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tours_list')
    else:
        form = TourForm()
    return render(request, 'add_tour.html', {'form': form})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients_list')
    else:
        form = ClientForm()
    return render(request, 'add_client.html', {'form': form})

def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookings_list')
    else:
        form = BookingForm()
    return render(request, 'add_booking.html', {'form': form})

def edit_client(request, client_id):
    client = get_object_or_404(Client, client_id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form, 'client': client})

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'edit_booking.html', {'form': form, 'booking': booking})

def edit_tour(request, tour_id):
    tour = get_object_or_404(Tour, tour_id=tour_id)
    if request.method == 'POST':
        form = TourForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('tours_list')
    else:
        form = TourForm(instance=tour)
    return render(request, 'edit_tour.html', {'form': form, 'tour': tour})