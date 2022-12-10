# Generated by Django 3.2.12 on 2022-12-10 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usersite', '0019_admission_details_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission_details',
            name='user',
        ),
        migrations.AddField(
            model_name='admission_details',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
