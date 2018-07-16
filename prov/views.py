from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Equipment, Emodel, Os, Vrf
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


class VrfListView(generic.ListView):
    model = Vrf
    paginate_by = 10


class VrfDetailView(generic.DetailView):
    model = Vrf


class EmodelListView(generic.ListView):
    model = Emodel
    paginate_by = 10


class EmodelDetailView(generic.DetailView):
    model = Emodel


class EquipmentCreate(CreateView):
    model = Equipment
    fields = '__all__'
    initial={'name':'ny-',}


class EquipmentUpdate(UpdateView):
    model = Equipment
    fields = ['name','playbook','inventory','os','equip_model']


class EquipmentDelete(DeleteView):
    model = Equipment
    success_url = reverse_lazy('equipment')
