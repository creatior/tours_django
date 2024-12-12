"""
URL configuration for tourdb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import main.views as view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.main_page),
    path('tours/', view.tours_list, name='tours_list'),
    path('tours/<int:tour_id>/', view.tour_detail, name='tour_detail'),
    path('tours/add/', view.add_tour, name='add_tour'),
    path('tours/edit/<int:tour_id>/', view.edit_tour, name="edit_tour"),
    path('clients/', view.clients_list, name='clients_list'),
    path('clients/add/', view.add_client, name='add_client'),
    path('clients/edit/<int:client_id>/', view.edit_client, name='edit_client'),
    path('bookings/', view.bookings_list, name='bookings_list'),
    path('bookings/add/', view.add_booking, name='add_booking'),
    path('bookings/edit/<int:booking_id>/', view.edit_booking, name='edit_booking'),
]

