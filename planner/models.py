from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    deadline = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title