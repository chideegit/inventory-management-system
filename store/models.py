from django.db import models
from django.contrib.auth.models import User

class Item(models.Model): 
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    restock_amount = models.IntegerField(default=0)
    recent_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Issue(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE)
    issued_to = models.CharField(max_length=100)
    quantity_issued = models.IntegerField()
    quantity_remaining = models.IntegerField()
    issued_on = models.DateField(auto_now_add=True)

class Receive(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    received_by = models.ForeignKey(User, on_delete=models.CASCADE)
    received_from = models.CharField(max_length=100)
    quantity_received = models.IntegerField()
    quantity_remaining = models.IntegerField()
    received_on = models.DateField(auto_now_add=True)




