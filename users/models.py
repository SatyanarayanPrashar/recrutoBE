from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    g_token = models.CharField(max_length=255, unique=True, default="")
    full_name = models.CharField(max_length=255)
    profile_photo = models.CharField(max_length=255, blank=True, null=True) 
    location = models.CharField(max_length=100, blank=True, null=True) 
    preferred_roles = models.CharField(max_length=255, blank=True, null=True) 
    bio = models.TextField(blank=True, null=True) 
    portfolio_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    anyother_link = models.URLField(blank=True, null=True)
    exp_title = models.CharField(max_length=255, blank=True, null=True)
    exp_company = models.CharField(max_length=255, blank=True, null=True) 
    exp_description = models.CharField(max_length=500, blank=True, null=True) 
    project_title = models.CharField(max_length=255, blank=True, null=True) 
    project_link = models.URLField(blank=True, null=True) 
    project_description = models.CharField(max_length=500, blank=True, null=True)  
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name
