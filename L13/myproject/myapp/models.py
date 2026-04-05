from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name