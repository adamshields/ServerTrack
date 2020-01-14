from django.db import models

class Team(models.Model):
    """
    Supports multiple Projects
    Supports multiple Servers within that project
    """
    name = models.CharField(max_length=200)
    # server = models.ManyToManyField("Server", related_name="team_server", verbose_name="Supported Servers", blank=True)
    # project = models.ManyToManyField("Project", related_name="team_projects", verbose_name="Supported Projects", blank=True)


    def __str__(self):
        return self.name

class Server(models.Model):
    """
    Servers are associated with Teams 
    Server can have multiple Teams that support it
    Servers are associated with a single project
    """
    name = models.CharField(max_length=200)
    # team = models.ManyToManyField("Team", related_name="team", verbose_name="Associated Teams for the Server", blank=True)
    # # team = models.ManyToManyField("Team", related_name="team_server", verbose_name="Associated Teams for the Server", blank=True) # BACKUP Change related_name
    # project = models.ForeignKey("Project", related_name="server_project", verbose_name="Associated Project", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    """
    Projects need show the Teams that Support the Project
    Projects need to show Servers associated with the Project

    """
    name = models.CharField(max_length=200)
    # team = models.ManyToManyField("Team", related_name="team", verbose_name="Teams that Support the Project", blank=True)
    # # team = models.ManyToManyField("Team", related_name="team_servers", verbose_name="Teams that Support the Project", blank=True) # BACKUP Change related_name
    # server = models.ManyToManyField("Server", related_name="project_servers", verbose_name="Servers associated with the Project", blank=True)

    def __str__(self):
        return self.name


