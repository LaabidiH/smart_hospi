# Generated by Django 5.0.4 on 2024-06-06 23:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_patient_chambre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='chambre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.chambre'),
        ),
    ]