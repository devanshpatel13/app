from django.db import models


# Create your models here.


class home(models.Model):


    name = models.CharField(max_length=20)
    number = models.IntegerField()
    email =models.EmailField()
    start_date= models.DateTimeField()
    end_date = models.DateTimeField()
