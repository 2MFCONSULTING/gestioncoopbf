from django.contrib import admin
from .models import Producteur, Campagne, Recolte

# Configuration pour afficher les colonnes dans l'administration
class ProducteurAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'village', 'telephone')
    search_fields = ('nom', 'village')

class RecolteAdmin(admin.ModelAdmin):
    list_display = ('producteur', 'produit', 'quantite', 'unite', 'campagne', 'date_reception')
    list_filter = ('produit', 'campagne', 'date_reception') # Ajoute des filtres sur le côté
    search_fields = ('producteur__nom', 'produit')

# Enregistrement des modèles
admin.site.register(Producteur, ProducteurAdmin)
admin.site.register(Campagne)
admin.site.register(Recolte, RecolteAdmin)