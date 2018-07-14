from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('equipment', views.EquipmentListView.as_view(), name='equipment'),
    path('equipment/<int:pk>', views.EquipmentDetailView.as_view(), name='equipment-detail'),

    path('emodel', views.EmodelListView.as_view(), name='emodel'),
    path('emodel/<int:pk>', views.EmodelDetailView.as_view(), name='emodel-detail')
]