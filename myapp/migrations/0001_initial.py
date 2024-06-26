# Generated by Django 5.0.6 on 2024-06-11 11:16

import datetime
import django.db.models.deletion
import django.utils.timezone
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
                ('ci', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('est_medecin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pointage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_pointage', models.DateTimeField(default=django.utils.timezone.now)),
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
        migrations.AddField(
            model_name='pointage',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.personnel'),
        ),
    ]
