from django.contrib import admin

from .models import Team, Server, Project 

# class TeamTabularInline(admin.TabularInline):
#     model = Team

class ServerTabularInline(admin.TabularInline):
    model = Server

# class ProjectTabularInline(admin.TabularInline):
#     model = Project

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ServerTabularInline]
    class Meta:
        model = Project

admin.site.register(Project, ProjectAdmin)





admin.site.register(Team)
admin.site.register(Server)
# admin.site.register(Project)

# class TeamAdmin(admin.ModelAdmin):

#     class Meta:
#         model = Team

# admin.site.register(Team, TeamAdmin)

# class TeamTabularInline(admin.TabularInline):
#     model = Team

# class ServerAdmin(admin.ModelAdmin):

#     class Meta:
#         model = Server

# admin.site.register(Server, ServerAdmin)

# class ServerTabularInline(admin.TabularInline):
#     model = Server

# class ProjectAdmin(admin.ModelAdmin):

#     class Meta:
#         model = Project

# admin.site.register(Project, ProjectAdmin)

# class ProjectTabularInline(admin.TabularInline):
#     model = Project

# # class ProjectManagerAdmin(admin.ModelAdmin):

# #     class Meta:
# #         model = ProjectManager

# # admin.site.register(ProjectManager, ProjectManagerAdmin)
