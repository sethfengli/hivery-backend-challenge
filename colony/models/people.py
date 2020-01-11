from django.db import models
from colony.models.company import Company
from colony.models.tag import Tag
from colony.models.fruit import Fruit
from colony.models.vegetable import Vegetable

class People(models.Model):
    _id = models.CharField(max_length=32,  blank=True) 
    index = models.IntegerField(null=False, primary_key=True, blank=False)
    guid = models.CharField(max_length=36, blank=False) 
    has_died = models.BooleanField(default=False, blank=False)
    balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    picture = models.CharField(max_length=255, blank=True) 
    age = models.IntegerField(null=False);
    eyeColor = models.CharField(max_length=100, blank=True) 
    name = models.CharField(max_length=255, blank=False) 
    gender = models.CharField(max_length=100, blank=True) 
    email = models.CharField(max_length=255, blank=True) 
    phone = models.CharField(max_length=255, blank=True) 
    address = models.CharField(max_length=255, blank=True) 
    about = models.CharField(max_length=1024, blank=True) 
    registered = models.DateTimeField( blank=True) 
    tags = models.ManyToManyField(Tag, blank=True)
    friends = models.ManyToManyField('self', symmetrical=False, blank=True )
    greeting = models.CharField(max_length=256, blank=True) 
    favouriteFood = models.CharField(max_length=1024, blank=True) 
    favouriteFruit = models.ManyToManyField(Fruit, blank=True)
    favouriteVegetable = models.ManyToManyField(Vegetable, blank=True)
    company = models.ForeignKey(Company,  on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Friend(People):

    class Meta:
        proxy = True
