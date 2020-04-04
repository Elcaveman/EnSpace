from django.db import models

# Create your models here.
class Application(models.Model):
    illustration = models.ImageField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.title