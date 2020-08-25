# Generated by Django 3.0.8 on 2020-08-25 10:15
import csv
import os.path
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.db import migrations

from apps.dishes import parser
from apps.dishes.models import Category, Dish


def add_category(apps, schema_editor):
    with open('./csv/category.csv', 'r') as file:
        reader = csv.reader(file)
        lst = list(reader)
        for row in lst:
            Category.objects.get_or_create(name=row[0])


def add_dishes(apps, schema_editor):
    queryset = Dish.objects.all()
    if not queryset.count():
        if not os.path.isfile('./csv/dishes.csv'):
            parser.main()
    with open('./csv/dishes.csv', 'r') as file:
        reader = csv.reader(file)
        lst = list(reader)
        for row in lst:
            category, _ = Category.objects.get_or_create(name=row[4])
            Dish.objects.get_or_create(name=row[0], category=category,
                                       price=row[1], description=row[5], weight=row[6])

            # загружаем в модель изображения из url
            response = requests.get(row[3])
            response_big = requests.get(row[2])
            name = urlparse(row[3]).path.split('/')[-1]
            name_big = urlparse(row[3]).path.split('/')[-1]
            dish = Dish.objects.get(name=row[0])
            dish.image.save(name, ContentFile(response.content), save=True)
            dish.image_big.save(name_big, ContentFile(response_big.content), save=True)


class Migration(migrations.Migration):
    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_category),
        migrations.RunPython(add_dishes),
    ]
