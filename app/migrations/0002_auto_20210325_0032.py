# Generated by Django 3.1.5 on 2021-03-25 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookashow',
            name='Ticket_price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
