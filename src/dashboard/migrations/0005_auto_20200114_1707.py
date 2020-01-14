# Generated by Django 3.0.2 on 2020-01-14 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200114_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='project',
            field=models.ManyToManyField(blank=True, related_name='team_projects', to='dashboard.Project', verbose_name='Supported Projects'),
        ),
        migrations.AddField(
            model_name='team',
            name='server',
            field=models.ManyToManyField(blank=True, related_name='team_server', to='dashboard.Server', verbose_name='Supported Servers'),
        ),
        migrations.AlterField(
            model_name='project',
            name='server',
            field=models.ManyToManyField(blank=True, related_name='project_servers', to='dashboard.Server', verbose_name='Servers associated with the Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(blank=True, related_name='team_servers', to='dashboard.Team', verbose_name='Teams that Support the Project'),
        ),
        migrations.AlterField(
            model_name='server',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_project', to='dashboard.Project', verbose_name='Associated Project'),
        ),
        migrations.AlterField(
            model_name='server',
            name='team',
            field=models.ManyToManyField(blank=True, related_name='team_server', to='dashboard.Team', verbose_name='Associated Teams for the Server'),
        ),
    ]
