from django.contrib import admin

# Register your models here.
from .models import Equipment, Emodel, Playbook, Inventory, Os

# admin.site.register(Equipment)
admin.site.register(Emodel)
admin.site.register(Playbook)
admin.site.register(Inventory)
admin.site.register(Os)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'equip_model', 'playbook', 'inventory', 'os')

admin.site.register(Equipment, EquipmentAdmin)
