# Generated by Django 2.2 on 2020-09-21 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('webapp', '0005_auto_20200831_0903'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name': 'ЗаказПродукт', 'verbose_name_plural': 'ЗаказыПродукты'},
        ),
        migrations.AddField(
            model_name='basket',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basket', to='sessions.Session'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='id_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_orders', to='webapp.Order', verbose_name='Id заказа'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='id_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_products', to='webapp.Product', verbose_name='Id продукта'),
        ),
    ]
