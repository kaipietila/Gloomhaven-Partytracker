from django.forms import ModelForm, CheckboxSelectMultiple
from core import models

class CreatePartyForm(ModelForm):
    class Meta:
        model = models.Party
        fields = [
            'name',
            'prosperity',
            'reputation',
            'completed_scenarios',
            ]
        widgets = {
        'completed_scenarios': CheckboxSelectMultiple(),
        }



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
        widgets = {
        'items': CheckboxSelectMultiple(),
        }


class CreateScenarioForm(ModelForm):
    class Meta:
        model = models.Scenario
        fields = [
            'name',
            'number',
            ]
