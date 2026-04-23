from django import forms
from .models import Producteur, Campagne, Recolte

class ProducteurForm(forms.ModelForm):
    class Meta:
        model = Producteur
        fields = ['nom', 'prenom', 'telephone', 'village']
        # On ajoute des classes Bootstrap pour le design
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'village': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CampagneForm(forms.ModelForm):
    class Meta:
        model = Campagne
        fields = ['nom', 'date_debut', 'date_fin', 'est_active']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'est_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
class RecolteForm(forms.ModelForm):
    class Meta:
        model = Recolte
        fields = ['producteur', 'campagne', 'produit', 'quantite', 'unite' ]
        
        # On ajoute des widgets pour que ce soit plus joli avec Bootstrap
        widgets = {
            'producteur': forms.Select(attrs={'class': 'form-control'}),
            'campagne': forms.Select(attrs={'class': 'form-control'}),
            'produit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Maïs, Coton...'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'unite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Kg, Tonnes'}),
            
        }        