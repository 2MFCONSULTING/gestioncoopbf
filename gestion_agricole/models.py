from django.db import models

# Module de gestion des campagnes agricoles (Objectif 4.30)
class Campagne(models.Model):
    nom = models.CharField(max_length=100) # ex: Campagne 2026
    date_debut = models.DateField()
    date_fin = models.DateField()
    est_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

# Module de gestion des membres (Objectif 4.29)
class Producteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, unique=True)
    village = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

# Module de gestion des intrants (Objectif 4.31)
class Intrant(models.Model):
    nom = models.CharField(max_length=100)
    stock_disponible = models.DecimalField(max_digits=10, decimal_places=2)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

class Recolte(models.Model):
    # Les liens (Clés étrangères)
    producteur = models.ForeignKey(Producteur, on_delete=models.CASCADE)
    campagne = models.ForeignKey(Campagne, on_delete=models.CASCADE)
    
    # Les infos de la récolte
    produit = models.CharField(max_length=100) # ex: Maïs, Coton, Sésame
    quantite = models.DecimalField(max_digits=10, decimal_places=2) # ex: 500.50
    unite = models.CharField(max_length=20, default="kg") # kg ou sacs
    date_reception = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.produit} - {self.producteur.nom} ({self.campagne.nom})"