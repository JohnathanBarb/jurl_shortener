from django.db import models

class Url(models.Model):
    token = models.CharField(max_length=5, unique=True, primary_key=True)
    url = models.TextField()
    expires_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
