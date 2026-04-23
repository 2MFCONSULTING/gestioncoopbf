from django.shortcuts import render, redirect, get_object_or_404
from .models import Producteur, Campagne, Recolte
from .forms import ProducteurForm, CampagneForm, RecolteForm

# Le reste de tes fonctions (ajouter_recolte, etc.) vient après

def liste_producteurs(request):
    producteurs = Producteur.objects.all()
    
    # On initialise le formulaire
    form = ProducteurForm()
    
    # Logique pour enregistrer les données quand on clique sur le bouton
    if request.method == 'POST':
        form = ProducteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_producteurs') # Recharge la page pour voir le nouveau membre
            
    # On ajoute 'form' dans le dictionnaire envoyé au template
    return render(request, 'gestion_agricole/liste_producteurs.html', {
        'producteurs': producteurs,
        'form': form
    })
def supprimer_producteur(request, pk):
    producteur = get_object_or_404(Producteur, pk=pk)
    producteur.delete()
    return redirect('liste_producteurs')
def liste_campagnes(request):
    campagnes = Campagne.objects.all().order_by('-date_debut') # Les plus récentes en premier
    form = CampagneForm()

    if request.method == 'POST':
        form = CampagneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_campagnes')

    return render(request, 'gestion_agricole/liste_campagnes.html', {
        'campagnes': campagnes,
        'form': form
    })
def modifier_producteur(request, pk):
    producteur = get_object_or_404(Producteur, pk=pk)
    if request.method == "POST":
        form = ProducteurForm(request.POST, instance=producteur)
        if form.is_valid():
            form.save()
            return redirect('liste_producteurs')
    else:
        form = ProducteurForm(instance=producteur)
    
    return render(request, 'gestion_agricole/modifier_producteur.html', {'form': form})
def supprimer_campagne(request, pk):
    campagne = get_object_or_404(Campagne, pk=pk)
    campagne.delete()
    return redirect('liste_campagnes')

def modifier_campagne(request, pk):
    campagne = get_object_or_404(Campagne, pk=pk)
    if request.method == "POST":
        form = CampagneForm(request.POST, instance=campagne)
        if form.is_valid():
            form.save()
            return redirect('liste_campagnes')
    else:
        form = CampagneForm(instance=campagne)
    
    return render(request, 'gestion_agricole/modifier_campagne.html', {'form': form})
def ajouter_recolte(request):
    toutes_les_recoltes = Recolte.objects.all().order_by('-date_reception')
    if request.method == 'POST':
        # Ici on UTILISE RecolteForm (il ne sera plus grisé)
        form = RecolteForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('ajouter_recolte') # On recharge la page pour voir la nouvelle ligne
        
            #return redirect('liste_producteurs')
    else:
        form = RecolteForm()
    
    return render(request, 'gestion_agricole/ajouter_recolte.html', {
        'form': form,
        'recoltes': toutes_les_recoltes  # On envoie la liste à la page HTML
    })
def modifier_recolte(request, pk):
    recolte = get_object_or_404(Recolte, pk=pk)
    if request.method == 'POST':
        form = RecolteForm(request.POST, instance=recolte)
        if form.is_valid():
            form.save()
            return redirect('ajouter_recolte')
    else:
        form = RecolteForm(instance=recolte)
    return render(request, 'gestion_agricole/ajouter_recolte.html', {'form': form, 'edit_mode': True})

def supprimer_recolte(request, pk):
    recolte = get_object_or_404(Recolte, pk=pk)
    if request.method == 'POST':
        recolte.delete()
        return redirect('ajouter_recolte')
    return render(request, 'gestion_agricole/supprimer_recolte_confirmer.html', {'recolte': recolte})