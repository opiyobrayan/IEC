# Generated by Django 4.1 on 2023-01-18 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec', '0003_books_alter_iec_order_with_respect_to_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]