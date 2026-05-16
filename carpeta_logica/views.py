import json
from django.shortcuts import render
import plotly.graph_objects as go
import plotly.io as pio
import requests
from django.http import JsonResponse


def home(request):
    return render(request, 'index.html')

def calculadora_de_inversion(request):
    # Por ahora renderiza simple, o puedes aplicar la misma lógica de backend aquí
    return render(request, 'calculadora-de-inversion.html')

def calculadora_de_valor_intrinseco(request):
    return render(request, 'calculadora-de-valor-intrinseco.html')

def calculadora_de_inflasion(request):
    return render (request, 'calculadora-de-inflasion.html')

def api_datos_ine(request):
    url_api = "https://servicios.ine.es/wstempus/js/es/DATOS_SERIE/IPC206305?nult=300"
    
    try:
        respuesta = requests.get(url_api, timeout=5)
        return JsonResponse(respuesta.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)