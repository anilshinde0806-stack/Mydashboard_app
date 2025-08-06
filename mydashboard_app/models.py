from django.db import models

class Sale(models.Model):
    product = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.product} - ₹{self.amount}"
