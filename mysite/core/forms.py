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

    def __init__(self, user, *args, **kwargs):
        super(CreateCharForm, self).__init__(*args, **kwargs)
        self.fields['party'].queryset = Party.objects.filter(user=creator)


class CreateScenarioForm(ModelForm):
    class Meta:
        model = models.Scenario
        fields = [
            'name',
            'number',
            ]
