from django.db import models

# Create your models here.
class Type(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Shop(models.Model):
    item=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.DecimalField(max_digits=5, decimal_places=2)
    img=models.ImageField(upload_to="shop")
    type=models.ForeignKey(Type,on_delete=models.CASCADE,default="")
    def __str__(self):
        return f"{self.item}-{self.type}"
    
class Cart(models.Model):
    item=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.DecimalField(max_digits=5, decimal_places=2)
    img=models.ImageField(upload_to="shop/cart")
    count=models.IntegerField(default=1)
    # type=models.ForeignKey(Type,on_delete=models.CASCADE,default="")
    def __str__(self):
        return f"{self.item}"
    @property
    def total_price(self):
        price= self.count*self.price
        return price