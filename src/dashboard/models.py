from django.db import models

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
    team = models.ManyToManyField(Team, verbose_name="Associated Teams")
    server = models.ManyToManyField(Server, verbose_name="Associated Servers")

    def __str__(self):
        return self.name


