# Generated by Django 5.1.6 on 2025-02-20 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciepe',
            name='reciepy_image',
            field=models.ImageField(upload_to='recipes/'),
        ),
    ]
