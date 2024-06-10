# Generated by Django 5.0.6 on 2024-06-06 22:52

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chambre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('etage', models.IntegerField()),
                ('temperature', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('humidite', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('qualite_air', models.CharField(default=0, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_entree', models.DateField()),
                ('date_sortie', models.DateField(default=datetime.date(2024, 1, 1))),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('est_medecin', models.BooleanField(default=False)),
                ('fonctionnalite', models.CharField(max_length=100)),
                ('date_pointage', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='chambre',
            constraint=models.UniqueConstraint(fields=('numero', 'etage'), name='unique_chambre'),
        ),
        migrations.AddField(
            model_name='patient',
            name='chambre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.chambre'),
        ),
    ]
