# Generated by Django 4.2.9 on 2024-08-27 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weightlifting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='startDate',
            new_name='compDate',
        ),
        migrations.RenameField(
            model_name='competition',
            old_name='name',
            new_name='compName',
        ),
    ]
