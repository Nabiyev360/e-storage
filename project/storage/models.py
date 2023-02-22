from django.db import models
from django.contrib.auth.models import User


class Rank(models.Model):
    rank=models.CharField(max_length=200)

    def __str__(self):
        return self.rank

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=30, null=True)
    profile_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=True, null=True, blank=False)
    is_new = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, default='def.png')

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    variants = (
        ('queue', 'Navbatda'),
        ('sendet', 'Yuborildi'),
        ('delivered', 'Yetkazildi'),
    )
    status = models.CharField(max_length=100, choices=variants)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.id)



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name