from django.db import models

# Create your models here.
class item(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=600,default="https://th.bing.com/th/id/R.78aab76606113ad8d781df4cfdfe4787?rik=g34KT78av2NJgg&pid=ImgRaw&r=0")

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50) 
    phone = models.CharField(max_length=10) 
    email = models.EmailField() 
    password = models.CharField(max_length=100) 
    nickname = models.CharField(max_length=100) 
    desc = models.CharField(max_length=200)


from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=50)

	@staticmethod
	def get_all_categories():
		return Category.objects.all()

	def __str__(self):
		return self.name
      





