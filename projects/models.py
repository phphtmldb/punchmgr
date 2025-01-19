from django.db import models

# Create your models here.


from django.db import models
from users.models import CustomUser

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class PunchList(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='punchlists')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    attachment = models.FileField(upload_to='attachments/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
