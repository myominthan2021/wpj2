# Generated by Django 3.2.9 on 2021-11-20 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellrecord', '0002_alter_sellrecord_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellrecord',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
