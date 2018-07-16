from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('emodel', views.EmodelListView.as_view(), name='emodel'),
    path('emodel/<int:pk>', views.EmodelDetailView.as_view(), name='emodel-detail')
]

urlpatterns += [
    path('equipment', views.EquipmentListView.as_view(), name='equipment'),
    path('equipment/<slug:slug>,<int:pk>', views.EquipmentDetailView.as_view(), name='equipment-detail'),

    path('equipment/create/', views.EquipmentCreate.as_view(), name='equipment_create'),
    path('equipment/<slug:slug>,<int:pk>/update/', views.EquipmentUpdate.as_view(), name='equipment_update'),
    path('equipment/<slug:slug>,<int:pk>/delete/', views.EquipmentDelete.as_view(), name='equipment_delete'),
]


urlpatterns += [
    path('vrf', views.VrfListView.as_view(), name='vrf'),
    path('vrf/<int:pk>', views.VrfDetailView.as_view(), name='vrf-detail'),

    path('vrf/create/', views.VrfCreate.as_view(), name='vrf_create'),
    path('vrf/<int:pk>/update/', views.VrfUpdate.as_view(), name='vrf_update'),
    path('vrf/<int:pk>/delete/', views.VrfDelete.as_view(), name='vrf_delete'),
]