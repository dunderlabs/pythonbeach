from django.shortcuts import render
from .models import Apoiador, Palestrante


def index(request):
    context = {}
    template_name = 'base.html'
    apoiadores = Apoiador.objects.all()
    palestrantes = Palestrante.objects.all()
    context['apoiadores'] = apoiadores
    context['palestrantes'] = palestrantes

    return render(request, template_name, context)
