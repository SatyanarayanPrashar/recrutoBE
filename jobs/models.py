from django.db import models

class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    company_mailid = models.CharField(max_length=100, default="NA")
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    remote_policy = models.CharField(max_length=30)

    def __str__(self):
        return self.title