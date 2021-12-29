from django.db import models


class Destination(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    discription=models.TextField()
    auther=models.IntegerField()
    image=models.ImageField(upload_to="pictures")
    offer=models.BooleanField(default=False)



class News(models.Model):
    image=models.ImageField(upload_to="blogs")
    date=models.IntegerField()
    month=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    disc=models.TextField()
