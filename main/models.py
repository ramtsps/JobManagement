from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    application_deadline = models.DateField()
    job_description = models.TextField()
