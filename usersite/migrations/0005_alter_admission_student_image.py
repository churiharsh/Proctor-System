# Generated by Django 4.0.1 on 2022-05-05 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0004_admission_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='student_image',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]