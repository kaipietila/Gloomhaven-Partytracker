from django.db import models
from django.core.validators import RegexValidator


item_id_validator = RegexValidator(r"^([0-9]{3},?){1,}$", "Enter the 3 digit item number")


class Party(models.Model):
    name = models.CharField(max_length=50)
    prosperity = models.IntegerField()
    reputation = models.CharField(max_length=50)

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
    items = models.CharField(validators=[item_id_validator], max_length=150)
    perks = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    party = models.ForeignKey(Party, default=None, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Brute(Character):
    """
    The Brute class
    """


class Tinkerer(Character):
    """
    The Tinkerer class
    """


class Scoundrel(Character):
    """
    The Scoundrel class
    """


class Mindthief(Character):
    """
    The Mindthief class
    """


class Cragheart(Character):
    """
    The Cragheart class
    """


class Paladin(Character):
    """
    The Paladin class
    """


class Item(models.Model):
    """
    Character Items, Using mainly the number to add to the character class
    """
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    item_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
