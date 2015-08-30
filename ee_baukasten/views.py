from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import EigenEntwicklung, Effektgruppe, Effekt


def index(request):
    template_name = 'index.html'
    ees = get_list_or_404(EigenEntwicklung.objects.order_by('name'))
    gruppen = get_list_or_404(Effektgruppe.objects.all())
    return render(request,
                  template_name,
                  {'ee_list': ees, 'gruppen': gruppen})


def ee_detail(request, ee_id):
    template_name = 'ee_detail.html'
    ee = get_object_or_404(EigenEntwicklung, pk=ee_id)
    effekte = get_list_or_404(ee.effekte.all())
    return render(request,
                  template_name,
                  {'ee': ee, 'effekte': effekte})


def effektgruppe(request, gruppe):
    template_name = 'effektgruppe.html'
    effekt_gruppe = get_object_or_404(Effektgruppe, pk=gruppe)
    # effekt_set bildet die umgekehrte Richtung der m2n Beziehung ab
    effekte = get_list_or_404(effekt_gruppe.effekt_set)
    return render(request,
                  template_name,
                  {'gruppe': effekt_gruppe, 'effekte': effekte})


def effekt(request, id):
    template_name = 'effekt.html'
    effekt = get_object_or_404(Effekt, pk=id)
    return render(request,
                  template_name,
                  {'effekt': effekt})
