# Generated by Django 3.1.1 on 2020-12-05 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metrica', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Consecucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
                ('meta', models.FloatField()),
                ('porcentaje_de_consecucion', models.FloatField()),
                ('objetivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.objetivo')),
            ],
        ),
    ]
