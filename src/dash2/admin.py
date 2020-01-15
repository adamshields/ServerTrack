from django.contrib import admin

# Register your models here.
from .models import Team, Server, Project, ProjectManager


class TeamAdmin(admin.ModelAdmin):

    class Meta:
        model = Team

admin.site.register(Team, TeamAdmin)

class TeamTabularInline(admin.TabularInline):
    model = Team

class ServerAdmin(admin.ModelAdmin):

    class Meta:
        model = Server

admin.site.register(Server, ServerAdmin)

class ServerTabularInline(admin.TabularInline):
    model = Server

class ProjectAdmin(admin.ModelAdmin):

    class Meta:
        model = Project

admin.site.register(Project, ProjectAdmin)

class ProjectTabularInline(admin.TabularInline):
    model = Project

class ProjectManagerAdmin(admin.ModelAdmin):

    class Meta:
        model = ProjectManager

admin.site.register(ProjectManager, ProjectManagerAdmin)


