# Generated by Django 3.2.12 on 2022-12-17 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0006_auto_20221217_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='current_semester',
            name='current_year',
            field=models.CharField(choices=[('FE', 'FE'), ('SE', 'SE'), ('TE', 'TE'), ('BE', 'BE')], max_length=50),
        ),
    ]
