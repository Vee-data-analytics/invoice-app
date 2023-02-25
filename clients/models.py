from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    client_address = models.TextField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    company_reg_no = models.CharField(max_length=20,null=True, blank=True) 
    vat_no =  models.CharField(max_length=10, null=True, blank=True)
    logo = models.ImageField(default='images/no_photo.png',blank=True)

    def __str__(self):
        return self.name

