from django.forms import ModelForm
from . import models

class CreatePartyForm(ModelForm):
    class Meta:
        model = models.Party
        fields = ['name', 'prosperity', 'reputation']


class CreateCharForm(ModelForm):
    class Meta:
        model = models.Character
        fields = [
            'name',
            'experience',
            'gold',
            'level',
            'items',
            'perks',
            'party',
            'character_class',
            ]
