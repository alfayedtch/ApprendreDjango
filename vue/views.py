from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    data = {'nom':'TCHAGNAO','prenom':'al-fayed', 'logiciel':['word','excel','powerPoint'],'age':19 }
    return HttpResponse(loader.get_template('index.html').render(data))