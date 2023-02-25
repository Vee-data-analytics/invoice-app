from pydoc import describe
from django.db import models
from invoice_app.models import Invoice
from profiles.models import Profiles
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



class Position(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True, help_text='optional')
    quantity = models.IntegerField(default=0, help_text='how many units?',blank=True)
    price = models.FloatField(default=0.00, help_text='in Rands',blank=True)
    amount = models.FloatField(null=True, help_text="in Rands")
    sub_total= models.FloatField(null=True ,blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)
