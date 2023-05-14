from django.db import models

# Create your models here.
class item(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=600,default="https://th.bing.com/th/id/R.78aab76606113ad8d781df4cfdfe4787?rik=g34KT78av2NJgg&pid=ImgRaw&r=0")

    def __str__(self):
        return self.name
