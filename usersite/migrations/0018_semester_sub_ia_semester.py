# Generated by Django 3.2.12 on 2022-12-23 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0017_auto_20221219_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester_sub_ia',
            name='semester',
            field=models.CharField(default=None, max_length=30),
        ),
    ]