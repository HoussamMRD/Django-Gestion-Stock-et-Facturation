from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html/', views.about, name='about us'),
    path('contact.html/', views.contact, name='contact us'),
    path('login.html/', views.loginEMP, name='login'),
    path('sign.html/', views.sign, name='sign'),
    path('servc.html/', views.service, name='service'),





    
    path('dashEMP.html/', views.dashEMP, name='dashEMP'),


    path('dashEMP.html/matstock.html/', views.Miss, name='Miss'),
    path('dashEMP.html/matstock.html/facture.html/', views.faq, name='facture'),
    path('dashEMP.html/matstock.html/facture.html/fct.html', views.fct, name='factre'),

    
    
    path('dashEMP.html/matstock.html/facture.html/question.html/', views.askQuestion, name='askQuestion'),
    path('dashEMP.html/matstock.html/facture.html/question.html/history.html/', views.questions, name='questions'),







]