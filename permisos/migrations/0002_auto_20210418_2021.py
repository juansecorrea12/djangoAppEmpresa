# Generated by Django 2.2 on 2021-04-18 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_auto_20210418_2021'),
        ('permisos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permisos',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='permisos',
            name='empleados',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empleados', to='empleados.Empleados'),
        ),
        migrations.AddField(
            model_name='permisos',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]