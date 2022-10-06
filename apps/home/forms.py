from django import forms


class ChecklistForm(forms.Form):
    location = forms.CharField(max_length=30)
    support = forms.CharField(max_length=30)
    bandPMA = forms.IntegerField(default=0, null=True, blank=True)
    bandPMO = forms.IntegerField(default=0, null=True, blank=True)
