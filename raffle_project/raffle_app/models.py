from django.db import models

class Raffle(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    prize = models.CharField(max_length=200)

    def __str__(self):
        return self.name