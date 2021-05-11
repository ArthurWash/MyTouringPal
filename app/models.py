from django.db import models
from django.forms import ModelForm

class BookAShow(models.Model):
    Band_name = models.CharField(max_length=64)
    Genre = models.CharField(
        max_length=2,
        choices=[
            ('RO', "Rock"),
            ('PU', "Punk"),
            ('ME', "Metal"),
            ('PO', "Pop"),
            ('HH', "Hip-Hop"),
            ('ED', "EDM")
        ]
    )
    Venue = models.CharField(
        max_length=2,
        choices=[
            ('BT', "BoonTunes"),
            ('ML', "MeatLocker"),
            ('BS', "Backroom Studios"),
            ('CB', "Championship Bar"),
            ('BB', "Brighton Bar"),
        ]
    )
    Requested_date = models.DateTimeField()
    Opening_Acts = models.CharField(max_length=256)
    Ticket_price = models.DecimalField(max_digits=4, decimal_places=2)
    Email = models.CharField(max_length=320)
    Additional_info = models.CharField(max_length=256)

class BookAShowForm(ModelForm):
    class Meta:
        model = BookAShow
        fields = ['Band_name', 'Genre', 'Venue', 'Requested_date', 'Opening_Acts', 'Ticket_price', 'Email', 'Additional_info']