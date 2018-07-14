from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Equipment, Emodel, Os

def index(request):
    num_equip = Equipment.objects.all().count()
    num_emodel = Emodel.objects.all().count()
    num_os = Os.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_equip':num_equip, 'num_emodel':num_emodel, 'num_os':num_os}
    )


class EquipmentListView(generic.ListView):
    model = Equipment
    paginate_by = 10


class EquipmentDetailView(generic.DetailView):
    model = Equipment


class EmodelListView(generic.ListView):
    model = Emodel
    paginate_by = 10


class EmodelDetailView(generic.DetailView):
    model = Emodel
