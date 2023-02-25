from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.forms import ValidationError
from django.contrib.auth.models import User



class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=13)
    company_name = models.CharField(max_length=200)
    company_address = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200,blank=True)
    company_reg_no = models.CharField(max_length=20,null=True, blank=True) 
    vat_no =  models.CharField(max_length=10, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    avatar =ProcessedImageField(upload_to='profilepics',
                                          processors=[ResizeToFill(100, 50)],
                                          format='JPEG',
                                          options={'quality':100})

    company_logo = ProcessedImageField(upload_to='company_logo',
                                          processors=[ResizeToFill(100, 50)],
                                          format='JPEG',
                                          options={'quality':100})

    def __str__(self):
        return f"Profile of the user,:{self.user.username}"

  