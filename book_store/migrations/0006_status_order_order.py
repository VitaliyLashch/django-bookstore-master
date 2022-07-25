# Generated by Django 4.0.2 on 2022-04-09 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_store', '0005_book_pages_alter_author_date_of_birth_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='status_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=200, verbose_name='Адреса')),
                ('phone', models.CharField(max_length=200, verbose_name='Телефон')),
                ('count', models.IntegerField(verbose_name='Кількість')),
                ('price', models.FloatField(verbose_name='Ціна')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book_store.book', verbose_name='Книга')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book_store.status_order', verbose_name='Статус замовлення')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Клієнт')),
            ],
        ),
    ]