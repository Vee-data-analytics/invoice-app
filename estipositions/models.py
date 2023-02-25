from django.db import models
from pydoc import describe
from django.db import models
from estimates.models import Estimate

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Position(models.Model):
    estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text='optional')
    quantity = models.IntegerField(default=0, help_text='how many units?',blank=True)
    price = models.FloatField(default=0.00, help_text='in Rands',blank=True)
    amount = models.FloatField(null=True, help_text="in Rands")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
