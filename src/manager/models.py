from django.conf import settings
from django.urls import reverse
from django.db import models

from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=300, unique=True, verbose_name='Project Name', blank=False, null=False)
    # slug = models.SlugField(unique=True, verbose_name='Project Slug')
    # short_name = models.CharField(max_length=300,verbose_name='Project Short Name', blank=True, null=True)
    # published_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    # created = models.DateTimeField(auto_now_add=True, verbose_name='Data Server was Created')
    # updated = models.DateTimeField(auto_now_add=True, verbose_name='Last Edited')    
    # last_reviewed = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    server = models.ManyToManyField('Server', related_name='+', blank=True)
    team = models.ManyToManyField('Team', related_name='+', blank=True)


    class Meta:
        verbose_name = ('Project')
        verbose_name_plural = ('Projects')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("project:project-detail", kwargs={"slug": self.slug})
 
    # def get_absolute_url(self):
    #     return reverse('project_detail', kwargs={'pk': self.pk})

class Server(models.Model):
    name = models.CharField(unique=True, max_length=400, verbose_name='Server Name')
    # slug = models.SlugField(unique=True, verbose_name='Server Slug')
    # ip_address = models.GenericIPAddressField(verbose_name='Server IP Address')
    # fqdn = models.CharField(max_length=300, verbose_name='FQDN', help_text='Enter FQDN', blank=True, null=True)
    # script = models.URLField(max_length=1000, verbose_name='Script BitBucket Url', help_text='Enter the URL of the BitBucket Repo', blank=True, null=True)
    # published_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    # created = models.DateTimeField(auto_now_add=True, verbose_name='Data Server was Created')
    # updated = models.DateTimeField(auto_now_add=True, verbose_name='Last Edited')    
    # last_reviewed = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    
    project = models.ForeignKey('Project', related_name='+', verbose_name='Associated Project', null=True, blank=True, on_delete = models.SET_NULL)
    team = models.ForeignKey('Team', related_name='+', verbose_name='Associated Team', null=True, blank=True, on_delete = models.SET_NULL)

    class Meta:
        verbose_name = ('Server')
        verbose_name_plural = ('Servers')
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('server_detail', kwargs={'slug': self.slug})

# def pre_save_server_slug(sender, instance, *args, **kwargs):
#     slug = slugify(instance.name)
#     instance.slug = slug

# pre_save.connect(pre_save_server_slug, sender=Server)



class Team(models.Model):
    name = models.CharField(max_length=300, unique=True, verbose_name='Team Name', blank=False, null=False)
    slug = models.SlugField(unique=True, verbose_name='Team Slug')
    published_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    # created = models.DateTimeField(auto_now_add=True, verbose_name='Data Server was Created')
    # updated = models.DateTimeField(auto_now_add=True, verbose_name='Last Edited')    
    # last_reviewed = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    server = models.ManyToManyField('Server', related_name='+', verbose_name='Associated Servers', blank=True)
    project = models.ManyToManyField('Project', related_name='+', verbose_name='Associated Projects', blank=True)

    class Meta:
        verbose_name = ('Team')
        verbose_name_plural = ('Teams')
        ordering = ["name"]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('team_detail', kwargs={'slug': self.slug})
 
    # def get_absolute_url(self):
    #     return reverse('team_detail', kwargs={'pk': self.pk})

# def pre_save_team_slug(sender, instance, *args, **kwargs):
#     slug = slugify(instance.name)
#     instance.slug = slug

# pre_save.connect(pre_save_team_slug, sender=Team)