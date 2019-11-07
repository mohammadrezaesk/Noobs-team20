from django.db import models


# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    text = models.TextField(max_length=250)

    def __str__(self):
        return self.title

class Course(models.Model):
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=100)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    first_day = models.CharField(max_length=10)
    second_day = models.CharField(max_length=10)

    def __str__(self):
        return self.name