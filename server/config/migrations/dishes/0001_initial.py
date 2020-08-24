# Generated by Django 3.0.8 on 2020-08-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='upload/dish')),
                ('price', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
                'ordering': ('id',),
            },
        ),
    ]
