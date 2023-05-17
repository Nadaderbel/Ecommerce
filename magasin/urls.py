from django.urls import path
from . import views
from .views import CategoryAPIView
urlpatterns = [
    path('', views.index,name='index'),
    path('nouveauFournisseur/',views.nouveauFournisseur,name='nouveauFournisseur'),
    path('category/',CategoryAPIView.as_view()),
    path('produit/', ProduitAPIView.as_view()),
    path('api/produit/<int:categorie>', views.ProduitAPIView.as_view()),
]
