
from django.db import models

class Thing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ## will detect the datetime when its updated

    def __str__(self):
        return self.title