from django.shortcuts import render, get_object_or_404
from .models import EigenEntwicklung

# Create your views here.


def index(request):
    template_name = 'index.html'
    ees = EigenEntwicklung.objects.order_by('name')
    return render(request, template_name, {'ee_list': ees})


def ee_detail(request, ee_id):
    template_name = 'ee_detail.html'
    ee = get_object_or_404(EigenEntwicklung, pk=ee_id)
    return render(request, template_name, {'ee': ee})
