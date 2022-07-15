# Generated by Django 4.0.6 on 2022-07-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True, null=True)),
                ('data_evento', models.DateTimeField()),
                ('data_criacao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
