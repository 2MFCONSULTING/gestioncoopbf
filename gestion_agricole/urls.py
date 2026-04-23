from django.urls import path
from . import views

urlpatterns = [
    path('producteurs/', views.liste_producteurs, name='liste_producteurs'),
    path('producteurs/', views.liste_producteurs, name='liste_producteurs'),
    path('producteur/supprimer/<int:pk>/', views.supprimer_producteur, name='supprimer_producteur'),
    path('producteur/modifier/<int:pk>/', views.modifier_producteur, name='modifier_producteur'),
    path('campagne/supprimer/<int:pk>/', views.supprimer_campagne, name='supprimer_campagne'),
    path('campagne/modifier/<int:pk>/', views.modifier_campagne, name='modifier_campagne'),
    path('recolte/', views.ajouter_recolte, name='ajouter_recolte'),
    path('recolte/modifier/<int:pk>/', views.modifier_recolte, name='modifier_recolte'),
    path('recolte/supprimer/<int:pk>/', views.supprimer_recolte, name='supprimer_recolte'),
]