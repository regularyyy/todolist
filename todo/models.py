from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    tag = models.CharField(max_length=50)
    due_date = models.DateField()
    is_complete = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

def __str__(self):
    return self.title