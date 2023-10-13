from django.db import models

# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10)
    # date = models.DateField()

    def __str__(self):
        return self.title
