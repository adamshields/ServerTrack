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

    list_display = ['id', 'name',]
    list_display_links = ['id', 'name']
    list_filter = ['id', 'name','team', 'server']
    # list_editable = ['name','short_name']
    # search_fields = ['id', 'name']
    class Meta:
        model = ProjectManager