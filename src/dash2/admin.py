from django.contrib import admin

# Register your models here.
from .models import Team, Server, Project, ProjectManager


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    class Meta:
        model = Team

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):

    class Meta:
        model = Server

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    class Meta:
        model = Project

@admin.register(ProjectManager)
class ProjectManagerAdmin(admin.ModelAdmin):

    class Meta:
        model = ProjectManager