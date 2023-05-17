from django.shortcuts import render
from django.template import loader
from .models import Produit,Fournisseur
from django.http import request
from .forms import ProduitForm,FournisseurForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer,ProduitSerializer


# Create your views here.
def index(request):
    if request.method == "POST" : 
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/magasin')
    else :
        form = ProduitForm() #créer formulaire vide
        list=Produit.objects.all()
    return render(request,'magasin/majProduits.html',{'form':form ,'list':list})
def nouveauFournisseur(request):
    if request.method == "POST" :
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            nouvFournisseur=Fournisseur.objects.all()
        return render(request,'magasin/vitrineF.html',{'nouvFournisseur':nouvFournisseur})
    else : 
        form = FournisseurForm() #créer formulaire vide 
        nouvFournisseur=Fournisseur.objects.all()
    return render(request,'magasin/fournisseur.html',{'form':form,'nouvFournisseur':nouvFournisseur})
class CategoryAPIView(APIView): 
    def get(self, *args, **kwargs):
                categories = Categorie.objects.all()
                serializer = CategorySerializer(categories, many=True)
                return Response(serializer.data)
class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
                produits=Produit.Object.all()
                serializer = ProduitSerializer(produits, many=True)
                return Response(serializer.data)

class ProductViewset(APIView):
    def get_queryset(self):
        queryset = Produit.objects.filter(active=True)
        category_id = self.request.GET.get('categorie')
        if category_id:
           queryset = queryset.filter(categorie=category_id)
        return queryset


 









   






    