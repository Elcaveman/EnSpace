from django.db import models
from django.contrib.auth.models import User


# TODO: custom Manager
class LearningObject(models.Model):
    #informations about the post owner
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #The post content
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    illustration = models.ImageField()
    description = models.CharField(max_length=200)
    #?files
    #?urls

    #informations about the audience-modulus
    branche = models.CharField(max_length=50)
    semester = models.IntegerField()
    modulus = models.CharField(max_length=100)
    element = models.CharField(max_length=50)
    #manager

    def __str__(self):
        return self.title

    # @classmethod
    # def recently_published(cls):
    #     return LearningObjectManager().all()
    #todo: optimizations:
    #make a model where the modules element is the PK
    #and get using it the "choices" for a drop list in the forms
