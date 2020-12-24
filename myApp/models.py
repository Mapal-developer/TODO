from django.db import models

# Create your models here.
class ToDo(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    due_date = models.DateField()
    def __str__(self):
        return self.name