from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='upload/dish', blank=True)
    price = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ('id',)
