# Generated by Django 2.1.3 on 2018-11-04 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id_mascota', models.AutoField(primary_key=True, serialize=False)),
                ('nom_mascota', models.CharField(max_length=20)),
                ('tamano_mascota', models.IntegerField(default=0)),
                ('peso_mascota', models.FloatField(default=0)),
                ('color_mascota', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=300)),
                ('fecha_rescate', models.DateField(verbose_name='Fecha Rescate')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rescatados.Estado')),
            ],
        ),
    ]
