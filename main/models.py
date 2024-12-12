from django.db import models

# экскурсия
class Tour(models.Model):
    tour_id = models.AutoField(primary_key=True, null=False, verbose_name="ID экскурсии")
    tour_name = models.CharField(max_length=150, null=False, verbose_name="Название")
    description = models.TextField(null=False, verbose_name="Описание")
    duration = models.IntegerField(null=False, verbose_name="Длительность")
    price = models.FloatField(null=False, verbose_name="Цена")

    def __str__(self):
        return self.tour_name

# клиент
class Client(models.Model):
    client_id = models.AutoField(primary_key=True, null=False, verbose_name="ID клиента")    
    surname = models.CharField(max_length=40, null=False, verbose_name="Фамилия")
    first_name = models.CharField(max_length=40, null=False, verbose_name="Имя")
    last_name = models.CharField(max_length=40, null=False,verbose_name="Отчество")
    email = models.EmailField(max_length=30, null=False, verbose_name="Адрес электронной почты")
    phone_number = models.CharField(max_length=15, null=False, verbose_name="Номер телефона")

    def __str__(self):
        return f"{self.first_name} {self.surname} {self.last_name}"

# бронирование
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True, null=False, verbose_name="ID бронирования")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False, verbose_name="Клиент")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=False, verbose_name="Экскурсия")
    booking_date = models.DateField(null=False, verbose_name="Дата бронирования")

    def __str__(self):
        return f"Booking {self.booking_id} for {self.tour.tour_name} by {self.client}"
