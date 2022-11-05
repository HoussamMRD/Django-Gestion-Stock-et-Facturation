from django.contrib import admin
from .models import Warehouse, Fournisseur, Produit, category, Question, Client,Facture





class  WarehouseAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'address', 'capacity_Stock')   
    list_filter = ('name', ) 
    search_fields = ( 'name', )



class FournisseurAdmin(admin.ModelAdmin):
    list_display = ( 'first_name', 'last_name', 'email', 'phone', 'name_product', 'QTT_Entree', 'Prix_Achat')
    list_filter = ('last_name' , 'name_product', )
    search_fields = (  'last_name' , 'name_product',)


class ProduitAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'reference', 'category',  'QTT_Stock', 'Prix_Stock', 'QTT_Entree', 'Prix_Achat', 'QTT_Sortie', 'Prix_Vente', 'Fournisseur', 'Warehouse')
    list_filter = ('name', )
    search_fields = ( 'name',)


class categoryAdmin(admin.ModelAdmin):
    list_display = ( 'title', )
    list_filter = ('title', )
    search_fields = ( 'title',)

class clientAdmin(admin.ModelAdmin):
    list_display = ( 'Nom', 'Prenom', 'phone', 'address',)
    list_filter = ('Prenom' , )
    search_fields = (  'Prenom' ,)

class FactureAdmin(admin.ModelAdmin):
    list_display = ( 'client', 'Produit', 'Mode_Paiement', 'Etat', 'QTT', 'Prix',)
    list_filter = ('client' ,'Produit', 'Mode_Paiement', 'Etat', )
    search_fields = (  'client' ,'Produit', 'Mode_Paiement', 'Etat',)




# Register your models here.
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Question)
admin.site.register(category, categoryAdmin)
admin.site.register(Client, clientAdmin)
admin.site.register(Facture, FactureAdmin)

