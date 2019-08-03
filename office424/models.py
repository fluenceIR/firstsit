from django.db import models

# Create your models here.


class PersonInfo(models.Model):
    name = models.CharField(max_length=20)
    cardID = models.CharField(max_length=12, primary_key=True)
    gender = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TradeInfo(models.Model):
    establish = models.DateField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    describe = models.CharField(max_length=100)
    person = models.ForeignKey(PersonInfo,on_delete=models.CASCADE)
    finish = models.DateField()

    def __str__(self):
        return self.describe
