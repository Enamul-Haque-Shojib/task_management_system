from django.db import models
from datetime import datetime
from categories.models import Category

# Create your models here.

class Task(models.Model):
    taskTitle = models.CharField(max_length=50, verbose_name='Task Title:')
    taskDescription = models.TextField(verbose_name='Task Description:')
    categories = models.ManyToManyField(Category)
    completed = models.BooleanField(default = False, verbose_name='Task Completed')
    date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.taskTitle

