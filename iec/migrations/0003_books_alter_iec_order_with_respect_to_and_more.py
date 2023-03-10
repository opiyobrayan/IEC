# Generated by Django 4.1 on 2023-01-18 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iec', '0002_rename_complete_iec_issued'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='IEC materirals', max_length=200, null=True)),
            ],
        ),
        migrations.AlterOrderWithRespectTo(
            name='iec',
            order_with_respect_to='created',
        ),
        migrations.AlterField(
            model_name='iec',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iec.books'),
        ),
    ]
