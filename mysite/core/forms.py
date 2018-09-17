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


        def __init__(self, creator, *args, **kwargs):
            super(CreateCharForm, self).__init__(*args, **kwargs)
            self.fields['party'].queryset=Party.objects.filter(creator=creator)


class CreateScenarioForm(ModelForm):
    class Meta:
        model = models.Scenario
        fields = [
            'name',
            'number',
            ]
