from django.db import models

# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    text = models.TextField(max_length=250)