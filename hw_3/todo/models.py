from django.db import models


class Thing(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=3000, default='')
    due_date = models.DateField(null=True, blank=True, auto_now_add=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'ID: {self.id} {self.title}'
