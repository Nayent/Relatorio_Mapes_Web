# Generated by Django 3.1.1 on 2020-09-24 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busca_consultas', '0002_auto_20200924_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exame',
            name='numero_guia_consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busca_consultas.consulta'),
        ),
    ]