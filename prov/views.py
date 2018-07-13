from django.shortcuts import render

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

