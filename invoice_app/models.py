from decimal import Decimal
from django.db.models import F, Sum
from xmlrpc import client
from django.db import models
from clients.models import Client
from profiles.models import Profiles 
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Invoice(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    clients = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=100)
    completion_date = models.DateField(null=True, blank=True)
    issued_date = models.DateField(null=True, blank=True)
    payement_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    payed= models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return f"Invoice; {self.invoice.invoice_number}, postion title: {self.title}"
    

    def __str__(self):
        return f"Invoice number: {self.invoice_number}, pk: {self.pk}"
  
    @property
    def tags(self):
        return self.tags.all()

    @property
    def positions(self):
        return self.position_set.all()

       
           
    '''
    @property
    def subtotal_amount(self):
        qs = self.positions
        subtotal = pos.quantity * pos.price == pos.sub_total
        for pos in qs:
            subtotal = pos.sub_total
        return subtotal
    
    
    @property
    def subtotal_amount(self):
        subtotal = 0
        qs = self.positions
        for pos in qs:
            subtotal =  pos.amount
        return subtotal

    '''            

    @property
    def total_amount(self):
        return self.positions.aggregate(
            total_price=Sum(F('quantity') * F('price'))
        )['total_price'] or Decimal('0')

