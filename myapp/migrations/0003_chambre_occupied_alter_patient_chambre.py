# Generated by Django 5.0.6 on 2024-06-05 23:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_patient_chambre'),
    ]

    operations = [
        migrations.AddField(
            model_name='chambre',
            name='occupied',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='chambre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.chambre'),
        ),
    ]
