from django.conf import settings
from django.urls import reverse
from django.db import models

from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

class Team(models.Model):
    """
    Supports multiple Projects
    Supports multiple Servers within that project
    """
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Server(models.Model):
    """
    Servers are associated with Teams 
    Server can have multiple Teams that support it
    Servers are associated with a single project
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Project(models.Model):
    """
    Projects need show the Teams that Support the Project
    Projects need to show Servers associated with the Project

    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProjectManager(models.Model):
    
    name = models.ForeignKey(Project, on_delete=models.CASCADE)
    team = models.ManyToManyField(Team, related_name="team_server", verbose_name="Teams that Support the Project", blank=True)
    server = models.ManyToManyField(Server, related_name="project_server", verbose_name="Associated Supported Servers", blank=True)
    
    # def __str__(self):
    #     return self.id
        
    def __str__(self):
        return str(self.name)
        
    def get_absolute_url(self):
		#url(r'^book/(?P<id>\d+)$', BookDetail.as_view(), name='book_detail'),
		#return reverse("book_detail", kwargs={"id": self.id})
        return reverse("projectmanager_detail", kwargs={"slug": self.slug})