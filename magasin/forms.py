from django.forms import ModelForm
from .models import Produit,Fournisseur
class ProduitForm(ModelForm): 
    class Meta :
        model = Produit
        fields = "__all__" 
        #pour tous les champs de la table
        #fields=['libelle','description'] #pour qulques champs
class FournisseurForm(ModelForm):
    class Meta : 
        model = Fournisseur
        fields = "__all__" #pour tous les champs de la table    


