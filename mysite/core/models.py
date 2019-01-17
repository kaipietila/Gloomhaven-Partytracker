from django.db import models
from django.contrib.auth.models import User


class Scenario(models.Model):
    """
    Basic scenario data. Parties can complete scenarios
    """
    name = models.CharField(max_length=150)
    number = models.IntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class Party(models.Model):
    """
    Party object that contains the characters.
    """
    name = models.CharField(max_length=50)
    prosperity = models.IntegerField()
    reputation = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    completed_scenarios = models.ForeignKey(Scenario, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Character_class(models.Model):
    """
    To make it easier to choose character class in the character creation.
    Data added to the db by default
    """
    name = models.CharField(max_length=50)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Item(models.Model):
    """
    Character Items, Using mainly the number to add to the character
    """
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    item_type = models.CharField(max_length=50)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Character(models.Model):
    """
    Basic Character class from Gloomhaven
    """
    name = models.CharField(max_length=50)
    experience = models.IntegerField()
    gold = models.IntegerField()
    level = models.IntegerField()
    items = models.ManyToManyField(Item)
    perks = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    party = models.ForeignKey(Party, default=None, on_delete=models.CASCADE)
    character_class = models.ForeignKey(Character_class, default=None,
                                        on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name