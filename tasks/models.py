from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50, default="Pending")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
