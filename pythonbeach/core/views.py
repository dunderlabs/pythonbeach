from django.shortcuts import render


def index(request):
    context = {}
    template_name = 'base.html'

    return render(request, template_name, context)
