from django.urls import path
from . import views

urlpatterns = [
    path('', views.mecanicos, name="mecanicos"),
    path('atualiza_mecanico/', views.att_mecanico, name="atualiza_mecanico"),
    path('update_mecanico/<int:id>', views.update_mecanico, name="update_mecanico")
]