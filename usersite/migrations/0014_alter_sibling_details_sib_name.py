# Generated by Django 3.2.12 on 2022-12-18 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0013_auto_20221218_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sibling_details',
            name='sib_name',
            field=models.CharField(default='NULL', max_length=50),
        ),
    ]