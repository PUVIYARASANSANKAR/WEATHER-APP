from django.db import models

class City(models.Model):
    name=models.TextField(max_length=150)

    def __str__(self):
        return self.city
