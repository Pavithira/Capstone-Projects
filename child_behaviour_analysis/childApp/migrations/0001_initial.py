# Generated by Django 3.0.2 on 2025-04-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='childModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blood_Glucose_Random', models.FloatField()),
                ('Blood_Urea', models.FloatField()),
                ('Serum_Creatine', models.FloatField()),
                ('Packed_cell_volume', models.FloatField()),
                ('White_blood_count', models.FloatField()),
            ],
        ),
    ]
