

from contextvars import Context
from django.shortcuts import render

def inicio(request):
    paginaweb = "index.html"
    contexto = {}
    
    return render(request, paginaweb, contexto)