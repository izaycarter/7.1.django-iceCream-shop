from django.db import models
from django.utils import timezone
from django.urls import reverse

import datetime

class IceCream(models.Model):

    CHOCOLATE = 'CHOCOLATE'
    VANILLA = 'VANILLA'

    BASE_CHOICES = [
        (CHOCOLATE, 'Chocolate'),
        (VANILLA, 'Vanilla'),
    ]

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    SEASONAL = "SEASONAL"

    AVAILABLE_CHOICES =[
        (DAILY, "Daily"),
        (WEEKLY, "Weekly"),
        (SEASONAL, "Seasonal"),
    ]

    flavor = models.CharField(max_length=255)
    base = models.CharField(max_length=255, choices=BASE_CHOICES, default=VANILLA)


    available = models.CharField(max_length=255, choices=AVAILABLE_CHOICES, default=WEEKLY)




    featured = models.BooleanField(default=False)
    date_churned = models.DateField("Date Churned", default=datetime.date.today)


    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.flavor

    def get_absolute_url(self):
        return reverse("ice_cream:index")
