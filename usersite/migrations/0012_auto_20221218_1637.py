# Generated by Django 3.2.12 on 2022-12-18 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0011_sibling_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family_info',
            old_name='address',
            new_name='paddress',
        ),
        migrations.RenameField(
            model_name='family_info',
            old_name='age',
            new_name='page',
        ),
        migrations.RenameField(
            model_name='family_info',
            old_name='contact_num',
            new_name='pcontact_num',
        ),
        migrations.RenameField(
            model_name='family_info',
            old_name='email',
            new_name='pemail',
        ),
        migrations.RenameField(
            model_name='family_info',
            old_name='name',
            new_name='pname',
        ),
        migrations.RenameField(
            model_name='family_info',
            old_name='occupation',
            new_name='poccupation',
        ),
        migrations.RenameField(
            model_name='family_info',
            old_name='qualification',
            new_name='pqualification',
        ),
        migrations.RenameField(
            model_name='family_info',
            old_name='relation',
            new_name='prelation',
        ),
    ]
