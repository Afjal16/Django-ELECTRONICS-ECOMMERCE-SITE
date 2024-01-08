import datetime
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Color(models.Model):
    name=models.CharField(max_length=200)
    code=models.CharField(max_length=70)
    
    def __str__(self):
        return self.name
    
class Filter_price(models.Model):
    FILTER_PRICE=(
        ('1000 TO 2000', '1000 TO 2000'),
        ('2000 TO 3000', '2000 TO 3000'),
        ('3000 TO 4000', '3000 TO 4000'),
        ('4000 TO 5000', '4000 TO 5000'),
        ('5000 TO 6000', '5000 TO 6000'),
    )
    price=models.CharField(max_length=70, choices=FILTER_PRICE)
    
    def __str__(self):
        return self.price
    

class Product(models.Model):
    CONDITION=(('NEW','NEW'),('OLD','OLD'))
    STOCK=(('IN STOCK','IN STOCK'),('OUT OF STOCK','OUT OF STOCK'))
    STATUS=(('PUBLISH','PUBLISH'),('DRAFT','DRAFT'))
    
    unique_id=models.CharField(unique=True,max_length=200, null=True,blank=True)
    image=models.ImageField(upload_to='product_image/img')
    name=models.CharField(max_length=200)
    price=models.FloatField()
    condition=models.CharField(choices=CONDITION, max_length=200)
    information=RichTextField(null=True)
    description=RichTextField(null=True)
    stock=models.CharField(choices=STOCK,max_length=200)
    status=models.CharField(choices=STATUS,max_length=200)
    created_date=models.DateTimeField(default=timezone.now)
    
    categories=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    filter_price=models.ForeignKey(Filter_price,on_delete=models.CASCADE)
    
    def save(self,*args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id=self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Images(models.Model):
    image=models.ImageField(upload_to='product_image/img')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
class Tag(models.Model):
    name=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    address=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    postcode=models.IntegerField(null=True)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=100)
    additional_info=models.TextField()
    amount=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True)
    date=models.DateTimeField(default=datetime.datetime.today)
    
    def __str__(self):
        return self.user.username
    
    
class orderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    product=models.CharField(max_length=250)
    image=models.ImageField(upload_to='product_image/Order_img')
    quantity=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    total=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.order.order.username