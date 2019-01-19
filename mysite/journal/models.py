from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    """
    Basic entry
    """
    header = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, default= None, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
