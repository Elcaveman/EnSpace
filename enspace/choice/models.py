from django.db import models

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    illustration = models.ImageField()
    
    def __str__(self):
        return self.title
    
    @property
    def get_app_name(self):
        return '/%s/'%self.name
