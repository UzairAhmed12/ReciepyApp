# Generated by Django 5.1.6 on 2025-02-19 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_student_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='File',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
