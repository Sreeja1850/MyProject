from django.db import models

class Task(models.Model):
    content = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content