from django.forms import ModelForm
from . import models

class CreatePartyForm(ModelForm):
    class Meta:
        model = models.Party
        fields = "__all__"


class CreateCharForm(ModelForm):
    class Meta:
        model = models.Character
        fields = "__all__"


class CreateScenarioForm(ModelForm):
    class Meta:
        model = models.Scenario
        fields = "__all__"
