# Generated by Django 3.0.2 on 2025-04-17 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('childApp', '0003_auto_20250416_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='childmodel',
            old_name='Age',
            new_name='Play_hours',
        ),
    ]
