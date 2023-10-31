from django.shortcuts import render, redirect

from .models import Maquina, Mancuerna, Barra
from .forms import CrearMancuernaFormulario, CrearMaquinaFormulario, CrearBarraFormulario, BusquedaMancuernaFormulario, BusquedaMaquinaFormulario, BusquedaBarraFormulario

def inicio(request):
    return render(request, 'inicio/inicio.html', {})

def maquinas(request):
    
    formulario = BusquedaMaquinaFormulario(request.GET)
    listado_de_maquinas = Maquina.objects.all()
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        if nombre_a_buscar: # Verifica si se proporciona un valor de búsqueda específico
            listado_de_maquinas = Maquina.objects.filter(nombre__icontains=nombre_a_buscar)
    
    formulario = BusquedaMaquinaFormulario()
    return render(request, 'inicio/maquinas.html', {'formulario': formulario, 'listado_de_maquinas': listado_de_maquinas})

def mancuernas(request):
    
    formulario = BusquedaMancuernaFormulario(request.GET)
    listado_de_mancuernas = Mancuerna.objects.all()
    if formulario.is_valid():
        peso_a_buscar = formulario.cleaned_data.get('peso')
        if peso_a_buscar:  # Verifica si se proporciona un valor de búsqueda específico
            listado_de_mancuernas = Mancuerna.objects.filter(peso=peso_a_buscar)
    
    formulario = BusquedaMancuernaFormulario()
    return render(request, 'inicio/mancuernas.html', {'formulario': formulario, 'listado_de_mancuernas': listado_de_mancuernas})

def barras(request):
    
    formulario = BusquedaBarraFormulario(request.GET)
    listado_de_barras = Barra.objects.all()
    if formulario.is_valid():
        tipo_a_buscar = formulario.cleaned_data.get('tipo')
        if tipo_a_buscar: # Verifica si se proporciona un valor de búsqueda específico
            listado_de_barras = Barra.objects.filter(tipo=tipo_a_buscar)
    
    formulario = BusquedaBarraFormulario()
    return render(request, 'inicio/barras.html', {'formulario': formulario, 'listado_de_barras': listado_de_barras})

def crear_maquina(request):
    
    if request.method == 'POST':
        formulario = CrearMaquinaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            # Valores de todos los productos
            marca = info_limpia.get('marca')
            precio = info_limpia.get('precio')
            
            # Específicos Maquina
            instrucciones_de_uso = info_limpia.get('instrucciones_de_uso')
            peso_limite = info_limpia.get('peso_limite')
            nombre = info_limpia.get('nombre')
            
            maquina = Maquina(marca=marca,precio=precio,instrucciones_de_uso=instrucciones_de_uso,peso_limite=peso_limite,nombre=nombre)
            maquina.save()
            
            return redirect('maquinas')
        else:
            return render(request, 'inicio/crear_maquina.html', {'formulario': formulario})
        
    formulario = CrearMaquinaFormulario()
    return render(request, 'inicio/crear_maquina.html', {'formulario': formulario})

def crear_mancuerna(request):
    
    if request.method == 'POST':
        formulario = CrearMancuernaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            # Valores de todos los productos
            marca = info_limpia.get('marca')
            precio = info_limpia.get('precio')
            
            # Específicos Mancuerna
            peso = info_limpia.get('peso')
            
            mancuerna = Mancuerna(marca=marca,precio=precio,peso=peso)
            mancuerna.save()
            
            return redirect('mancuernas')
        else:
            return render(request, 'inicio/crear_mancuerna.html', {'formulario': formulario})
        
    formulario = CrearMancuernaFormulario()
    return render(request, 'inicio/crear_mancuerna.html', {'formulario': formulario})

def crear_barra(request):
    
    if request.method == 'POST':
        formulario = CrearBarraFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            # Valores de todos los productos
            marca = info_limpia.get('marca')
            precio = info_limpia.get('precio')
            
            # Específicos Maquina
            tipo = info_limpia.get('tipo')
            peso = info_limpia.get('peso')
            
            barra = Barra(marca=marca,precio=precio,tipo=tipo,peso=peso)
            barra.save()
            
            return redirect('barras')
        else:
            return render(request, 'inicio/crear_barra.html', {'formulario': formulario})
        
    formulario = CrearBarraFormulario()
    return render(request, 'inicio/crear_barra.html', {'formulario': formulario})