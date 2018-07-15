from django.contrib import admin

# Register your models here.
from .models import Equipment, Emodel, Playbook, Inventory, Os, Vrf, Vlan

# admin.site.register(Equipment)
admin.site.register(Emodel)
admin.site.register(Playbook)
admin.site.register(Inventory)
admin.site.register(Os)
#admin.site.register(Vrf)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'equip_model', 'playbook', 'inventory', 'os')

admin.site.register(Equipment, EquipmentAdmin)


class VrfAdmin(admin.ModelAdmin):
    list_display = ('name', 'equipment', 'loopback', 'linknet')
    list_filter = ['name']

admin.site.register(Vrf, VrfAdmin)


class VlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'vlan_id', 'network_addr', 'vrf')

admin.site.register(Vlan, VlanAdmin)
