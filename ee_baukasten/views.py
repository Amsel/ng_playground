from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import EigenEntwicklung, Effektgruppe

# Create your views here.


def index(request):
    template_name = 'index.html'
    ees = get_list_or_404(EigenEntwicklung.objects.order_by('name'))
    gruppen = get_list_or_404(Effektgruppe.objects.all())
    return render(request, template_name, {'ee_list': ees, 'gruppen': gruppen})


def ee_detail(request, ee_id):
    template_name = 'ee_detail.html'
    ee = get_object_or_404(EigenEntwicklung, pk=ee_id)
    effekte = get_list_or_404(ee.effekte.all())
    return render(request, template_name, {'ee': ee, 'effekte': effekte})
