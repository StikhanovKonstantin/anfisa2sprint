from django.shortcuts import render

from ice_cream.models import IceCream

from django.db.models import Q


def index(request):
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description',
    ).filter(
        Q(is_published=True)
        & Q(is_on_main=True)
        & Q(category__is_published=True)
    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, 'homepage/index.html', context)
