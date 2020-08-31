# Generated by Django 3.0.8 on 2020-08-25 10:15
import csv

from django.db import migrations

from apps.orders.models import Status


def add_status(apps, schema_editor):
    with open('./csv/status.csv', 'r') as file:
        reader = csv.reader(file)
        lst = list(reader)
        for row in lst:
            Status.objects.get_or_create(name=row[0])


class Migration(migrations.Migration):
    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_status),
    ]