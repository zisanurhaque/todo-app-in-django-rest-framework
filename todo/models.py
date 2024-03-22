from django.db import models

# Create your models here.
class TodoModel(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('on-going', 'On-Going'),
        ('completed', 'Completed')
    ]
    title = models.CharField(max_length = 200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length = 100, choices = STATUS_CHOICES)

    def __str__(self):
        return self.title
