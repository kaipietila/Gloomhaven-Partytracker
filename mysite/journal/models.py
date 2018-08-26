from django.db import models


class Entry(models.Model):
    """
    Basic entry
    """
    project = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.body


