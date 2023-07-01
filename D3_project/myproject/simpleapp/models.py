from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(
        max_length=200,
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0, 'Quantity should be >= 0')],
    )

    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    price = models.FloatField(validators=[MinValueValidator(0.0, 'Price should be >= 0.0')])

    def __str__(self):
        return f'{self.name}: {self.quantity}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/products/{self.id}'

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'