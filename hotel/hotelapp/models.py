from django.db import models

# Create your models here.
class Hotel(models.Model):
    img=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Booking(models.Model):
    cus_name=models.CharField(max_length=55)
    cus_phone=models.CharField(max_length=12)
    name=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    checkin_date=models.DateField()
    checkout_date=models.DateField()