# Generated by Django 3.0.2 on 2020-01-15 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmanager',
            name='project_servers',
            field=models.ManyToManyField(blank=True, related_name='project_server', to='dash2.Server', verbose_name='Associated Supported Servers'),
        ),
        migrations.AlterField(
            model_name='projectmanager',
            name='project_team_servers',
            field=models.ManyToManyField(blank=True, related_name='team_server', to='dash2.Team', verbose_name='Teams that Support the Project'),
        ),
    ]