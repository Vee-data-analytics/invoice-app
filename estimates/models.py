from decimal import Decimal
from django.db.models import F, Sum
from django.db import models
import profile
from django.db import models
from clients.models import Client
from profiles.models import Profiles 

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Estimate(models.Model):
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    clients = models.ForeignKey(Client, on_delete=models.CASCADE)
    estimate_number = models.CharField(max_length=100)
    completion_date = models.DateField(null=True, blank=True)
    issued_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    payed= models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return f"Invoice; {self.invoice.estimate_number}, postion title: {self.title}"
    

    def __str__(self):
        return f"Invoice number: {self.estimate_number}, pk: {self.pk}"
  
    @property
    def tags(self):
        return self.tags.all()

    @property
    def positions(self):
        return self.position_set.all()

    @property
    def total_amount(self):
        return self.positions.aggregate(
            total_price=Sum(F('quantity') * F('price'))
        )['total_price'] or Decimal('0')
        