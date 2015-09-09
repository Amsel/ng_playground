from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import PlayerCreation, EffectCategory, Effect


def index(request):
    template_name = 'index.html'
    player_creations = get_list_or_404(PlayerCreation.objects.order_by('name'))
    categories = get_list_or_404(EffectCategory.objects.all())
    return render(request,
                  template_name,
                  {'ee_list': player_creations, 'gruppen': categories})


def ee_detail(request, ee_id):
    template_name = 'ee_detail.html'
    pc = get_object_or_404(PlayerCreation, pk=ee_id)
    effects = get_list_or_404(pc.effekte.all())
    return render(request,
                  template_name,
                  {'ee': pc, 'effekte': effects})


def effektgruppe(request, gruppe):
    template_name = 'effektgruppe.html'
    effect_category = get_object_or_404(EffectCategory, pk=gruppe)

    # effect_set uses the m2m relation in reverse
    effects = get_list_or_404(effect_category.effect_set)
    return render(request,
                  template_name,
                  {'gruppe': effect_category, 'effekte': effects})


def effekt(request, id):
    template_name = 'effekt.html'
    effect = get_object_or_404(Effect, pk=id)
    return render(request,
                  template_name,
                  {'effekt': effect})
