from django.db import models
from django.contrib.auth.models import User

class Audience(models.Model):
    #this model is acceccisble only by the admin in case a new modulus is added or delete
    BRANCHES = [('GL', 'Génie logiciel'),
    ('eMBI', 'e-Management and Business Intelligence'),
    ('IeL', 'Ingénierie e-Logistique'),
    ('ISEM', 'Ingénierie des Systèmes Embarqués et Mobiles'),
    ('IWIM', 'Ingénierie du Web et Informatique Mobile'),
    ('SSI', "Sécurité des Systèmes d'Information"),
    ('2IA', 'Ingénierie Intelligence Artificielle'),
    ('IF', 'Ingénierie Digitale pour la Finance ')
    ]

    SEMESTERS = [("S%d"%i,)*2 for i in range(1,6)]
    #dynamic choices (need forms)
    element = models.CharField(max_length=100)
    modulus = models.CharField(max_length=100)
    #fix choices
    semester = models.CharField(max_length=80,
    choices = SEMESTERS)
    branche = models.CharField(max_length=80,
    choices = BRANCHES)
    def __str__(self):
        return self.element
    
    
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
    audience = models.ForeignKey("Audience", on_delete=models.CASCADE , null=True)
    #manager

    def __str__(self):
        return self.title

    # @classmethod
    # def recently_published(cls):
    #     return LearningObjectManager().all()
    #todo: optimizations:
    #make a model where the modules element is the PK
    #and get using it the "choices" for a drop list in the forms



    