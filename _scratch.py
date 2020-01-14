from django.db import models

class Team(models.Model):
    """
    Supports a Project
    Supports Servers within that project
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
class Server(models.Model):
    """
    What Team Supports the Server
    What Project its under
    Server Can only be associated with 1 project
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Project(models.Model):
    """
    What servers are under the project
    what team supports the project
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


