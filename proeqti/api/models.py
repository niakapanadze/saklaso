from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"ეს არის პროდუქტი - self.name"


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(null=True, blank=True)

    def __str__(self):
        return f"მომხმარებელი - {self.first_name} {self.last_name}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    amount = models.IntegerField()

    def __str__(self):
        return f"შეკვეთა არის ეს - #{self.id} - {self.customer}"
