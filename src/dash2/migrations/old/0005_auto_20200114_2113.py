# Generated by Django 3.0.2 on 2020-01-15 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash2', '0004_auto_20200114_2112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectmanager',
            old_name='name',
            new_name='project_name',
        ),
        migrations.RenameField(
            model_name='projectmanager',
            old_name='server',
            new_name='project_servers',
        ),
        migrations.RenameField(
            model_name='projectmanager',
            old_name='team',
            new_name='project_team_servers',
        ),
    ]
