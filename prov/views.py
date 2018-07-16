from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Equipment, Emodel, Os, Vrf, Vlan
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

class VrfListView(generic.ListView):
    model = Vrf
    paginate_by = 10


class VrfDetailView(generic.DetailView):
    model = Vrf


class VrfCreate(CreateView):
    model = Vrf
    fields = '__all__'
    initial={'loopback':'/32','linknet':'/31'}


class VrfUpdate(UpdateView):
    model = Vrf
    fields = ['name','equipment','loopback','linknet']


class VrfDelete(DeleteView):
    model = Vrf
    success_url = reverse_lazy('vrf')


class VlanDetailView(generic.DetailView):
    model = Vlan


class VlanCreate(CreateView):
    model = Vlan
    fields = '__all__'


class VlanUpdate(UpdateView):
    model = Vlan
    fields = ['name','vlan_id','network_addr','vrf']
    success_url = reverse_lazy('vrf')


class VlanDelete(DeleteView):
    model = Vlan
    success_url = reverse_lazy('vrf')


class EmodelListView(generic.ListView):
    model = Emodel
    paginate_by = 10


class EmodelDetailView(generic.DetailView):
    model = Emodel

