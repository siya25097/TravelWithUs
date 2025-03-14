from django.db import models

class BookNow(models.Model):
    name = models.CharField(max_length=100, db_column='Name')
    email = models.EmailField(db_column='Email')
    booking_date = models.DateField(db_column='Booking_Date')
    guests = models.IntegerField(db_column='Guests')

    def __str__(self):
        return f"Booking by {self.name} for {self.guests} guests"
