# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-02 17:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encuesta',
                'verbose_name_plural': 'Encuestas',
            },
        ),
        migrations.CreateModel(
            name='OpcionPregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'OpcionPregunta',
                'verbose_name_plural': 'OpcionPreguntas',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('PA', 'Abierta'), ('PC', 'Cerrada'), ('POM', 'Opcion Multiple')], max_length=2)),
                ('titulo', models.CharField(max_length=300)),
                ('descripcion', models.TextField()),
                ('obligatoria', models.BooleanField()),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name': 'Pregunta',
                'verbose_name_plural': 'Preguntas',
            },
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(max_length=500)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.Pregunta')),
            ],
            options={
                'verbose_name': 'Resultado',
                'verbose_name_plural': 'Resultados',
            },
        ),
        migrations.AddField(
            model_name='opcionpregunta',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.Pregunta'),
        ),
    ]
