from django.db import models
class Reg(models.Model):
    User=models.CharField(primary_key=True,max_length=20)
    Pwd=models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    Dob=models.DateField()
    mobno=models.IntegerField()
    # Create your models here.
