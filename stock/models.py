from queue import LifoQueue
from turtle import title
from unicodedata import category, name
from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    capacity_Stock = models.CharField(max_length=20)
   

    def __str__(self):
        return self.name


class Fournisseur(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    name_product = models.CharField(max_length=100)
    QTT_Entree = models.CharField(max_length=100)
    Prix_Achat = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name



class category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Produit(models.Model):
    name = models.CharField(max_length=100)
    reference=models.CharField(max_length=100)
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    QTT_Stock = models.CharField(max_length=100)
    Prix_Stock = models.CharField(max_length=100)
    QTT_Entree = models.CharField(max_length=100)
    Prix_Achat = models.CharField(max_length=100)
    QTT_Sortie = models.CharField(max_length=100)
    Prix_Vente = models.CharField(max_length=100)
    Fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    Warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.name










class Question(models.Model):
    description =models.CharField(max_length=500)
    admin_comment=models.CharField(max_length=200,default='Nothing')
    asked_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.description







class Client(models.Model):
    Nom = models.CharField(max_length=100,null=True)
    Prenom = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    RIB=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.Prenom



class Facture(models.Model):
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    Produit=models.ForeignKey(Produit, on_delete=models.CASCADE)
    date=models.DateTimeField(null=True)
    Mode_Paiement=models.CharField(max_length=100,null=True,choices=[( 'Especes','Especes'),( 'Cheque',' Cheque'),('Versement','Versement'),(' Virement',' Virement'),('Autre','Autre')])
    Etat=models.CharField(max_length=100,null=True,choices=[( 'Non Paye','Non Paye'),( 'Payé','Payé'),('Verse','Verse'),('Annulé','Annulé')])
    TVA=models.CharField(max_length=100,null=True)
    QTT=models.CharField(max_length=100,null=True)
    Prix=models.CharField(max_length=100,null=True)
    Total=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.client.Nom