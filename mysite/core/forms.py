from django.forms import ModelForm
from . import models

class CreatePartyForm(ModelForm):
    class Meta:
        model = models.Party
        fields = [
            'name',
            'prosperity',
            'reputation',
            'completed_scenarios',
            ]


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


class CreateScenarioForm(ModelForm):
    class Meta:
        model = models.Scenario
        fields = [
            'name',
            'number',
            ]
