# from django.shortcuts import render #Próximamente...
from django.http import HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse('Osea Jelou')


def about(request):
    return HttpResponse('About')