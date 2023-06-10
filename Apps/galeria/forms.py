from django import forms
from Apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels = {
            'Descricao': 'descrição',
            'usuario':'Propietário',
            'data_Publicada':'Data de Registro'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),

            'data_Publicada': forms.DateInput(attrs={
                'class': 'form-control',
                 'type': 'date'
                 },
            format= '%d/%m/%Y'),

            'usuario': forms.Select(attrs={'class': 'form-control'}),


        }