# Generated by Django 3.0.4 on 2020-06-09 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mood',
            old_name='moode_text',
            new_name='mood_text',
        ),
    ]
