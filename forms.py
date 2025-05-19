from django import forms
class Eoform(forms.Form):
    num=forms.IntegerField(label="Enter number",
    widget=forms.NumberInput(attrs={"placeholder":"type here..."}))