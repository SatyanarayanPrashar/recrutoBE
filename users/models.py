from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    g_token = models.CharField(max_length=255, unique=True, default="")
    full_name = models.CharField(max_length=255)
    profile_photo = models.CharField(max_length=255, default="NA")
    location = models.CharField(max_length=100)
    preferred_roles = models.CharField(max_length=255)
    bio = models.TextField()
    portfolio_link = models.URLField()
    linkedin_link = models.URLField()
    github_link = models.URLField()
    anyother_link = models.URLField(blank=True)
    exp_title = models.CharField(max_length=255)
    exp_company = models.CharField(max_length=255)
    exp_description = models.CharField(max_length=500)
    project_title = models.CharField(max_length=255)
    project_link = models.URLField()
    project_description = models.CharField(max_length=500)
    skills = models.TextField()

    def __str__(self):
        return self.full_name