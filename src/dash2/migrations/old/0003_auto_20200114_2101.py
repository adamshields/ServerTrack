# Generated by Django 3.0.2 on 2020-01-15 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash2', '0002_auto_20200114_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmanager',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='dash2.Project'),
        ),
    ]
