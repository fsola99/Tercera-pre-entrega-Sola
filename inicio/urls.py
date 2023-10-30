from django.urls import path
from inicio.views import inicio, maquinas, mancuernas, barras, crear_maquina, crear_mancuerna, crear_barra

urlpatterns = [
    path('', inicio, name='inicio'),
    path('mancuernas/', mancuernas, name='mancuernas'),
    path('maquinas/', maquinas, name='maquinas'),
    path('barras/', barras, name='barras'),
    path('mancuernas/crear/', crear_mancuerna, name='crear_mancuerna'),
    path('maquinas/crear/', crear_maquina, name='crear_maquina'),
    path('barras/crear/', crear_barra, name='crear_barra')
]