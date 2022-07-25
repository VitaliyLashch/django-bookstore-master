# Generated by Django 4.0.2 on 2022-04-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0007_alter_order_options_order_date_finish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_finish',
            field=models.DateField(blank=True, null=True, verbose_name='Дата прибуття'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_start',
            field=models.DateField(blank=True, null=True, verbose_name='Дата відправки'),
        ),
    ]