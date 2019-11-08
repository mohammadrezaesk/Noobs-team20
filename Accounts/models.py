from django.contrib.auth.models import User
from django.db import models

from Home.models import Course


class x(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, upload_to='media/static/images')

    def __str__(self):
        return self.user.username
