from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('equipment', views.EquipmentListView.as_view(), name='equipment'),
    path('equipment/<slug:slug>,<int:pk>', views.EquipmentDetailView.as_view(), name='equipment-detail'),

    path('vrf', views.VrfListView.as_view(), name='vrf'),
    path('vrf/<int:pk>', views.VrfDetailView.as_view(), name='vrf-detail'),

    path('emodel', views.EmodelListView.as_view(), name='emodel'),
    path('emodel/<int:pk>', views.EmodelDetailView.as_view(), name='emodel-detail')
]