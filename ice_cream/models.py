from django.db import models
from django.utils import timezone

class Icecream(models.Model):
    ice_cream_text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.ice_cream_text


class Choice(models.Model):
    section = models.ForeignKey(Icecream, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    featured = models.BooleanField(default=False)
    churned_date = models.DateTimeField("date Churned", default=timezone.now)

    def __str__(self):
        return self.choice_text
