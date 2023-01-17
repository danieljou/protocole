from django import forms
from .models import *


class EtudiantForm(forms.ModelForm):
    
    class Meta:
        model = Etudiant
        fields = ("__all__")

class CritereForm(forms.ModelForm):
    
    class Meta:
        model = Critere
        fields = ("__all__")


class NoteForm(forms.ModelForm):

    class Meta:
        model = note
        fields = ("note",)


class NotationForm(forms.ModelForm):
    
    class Meta:
        model = Notation
        exclude = ('etudiant','utilisateur')

    



