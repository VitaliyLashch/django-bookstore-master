# Generated by Django 4.0.2 on 2022-04-09 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0003_remove_author_name_author_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]