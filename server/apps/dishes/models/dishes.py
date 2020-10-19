from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)


class Dish(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='dishes/', blank=True)
    image_big = models.ImageField(upload_to='dish_big/', blank=True)
    price = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weight = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ('id',)
