from django.db import models

# Create your models here.
class Posting(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=30)
    releasedat=models.DateField()
    
    def __str__(self):
        return "{}".format(self.title)

