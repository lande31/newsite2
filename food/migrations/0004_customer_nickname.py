# Generated by Django 4.2.1 on 2023-10-14 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='nickname',
            field=models.CharField(default='lade', max_length=100),
            preserve_default=False,
        ),
    ]
