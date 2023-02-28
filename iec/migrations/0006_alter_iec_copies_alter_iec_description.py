# Generated by Django 4.1 on 2023-01-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iec', '0005_iec_thematic_alter_iec_copies_alter_iec_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iec',
            name='copies',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='iec',
            name='description',
            field=models.CharField(blank=True, choices=[('Book', 'Book'), ('Fliers', 'Fliers'), ('Poster', 'Poster'), ('Notebook', 'Notebook'), ('Booklet', 'Booklet')], max_length=200, null=True),
        ),
    ]
