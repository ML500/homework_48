# Generated by Django 2.2 on 2020-07-30 17:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Остаток'),
        ),
    ]