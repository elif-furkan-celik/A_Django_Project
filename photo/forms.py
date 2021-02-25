from django import forms
from .models import Photos

class UpdateForm0(forms.ModelForm):
    class Meta:
        model = Photos
        fields = [
            'answer10',
            'answer20',
            'answer30',
        ]

class UpdateForm1(forms.ModelForm):
    class Meta:
        model = Photos
        fields = [
            'answer11',
            'answer21',
            'answer31',
        ]
        
class UpdateForm2(forms.ModelForm):
    class Meta:
        model = Photos
        fields = [
            'answer12',
            'answer22',
            'answer32',
        ]
        
class UpdateForm3(forms.ModelForm):
    class Meta:
        model = Photos
        fields = [
            'answer13',
            'answer23',
            'answer33',
        ]
        
class UpdateForm4(forms.ModelForm):
    class Meta:
        model = Photos
        fields = [
            'answer14',
            'answer24',
            'answer34',
        ]