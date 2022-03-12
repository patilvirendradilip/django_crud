from django.db import models

# Create your models here.


class StudentModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    dob = models.DateField()
    CHOICES = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(choices=CHOICES, max_length=128)


