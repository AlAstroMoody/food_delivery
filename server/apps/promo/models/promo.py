from django.db import models


class Promo(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='promo/', blank=True)

    class Meta:
        verbose_name = 'Изображение на слайдер'
        verbose_name_plural = 'Изображения на слайдер'

    def __str__(self):
        return self.name
