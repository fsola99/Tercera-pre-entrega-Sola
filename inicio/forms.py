from django import forms

#from .models import Mancuerna,Maquina,Barra
    
class CrearMancuernaFormulario(forms.Form):
    # Valores de todos los productos
    marca = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    
    # Específicos Mancuerna
    peso = forms.IntegerField()
    
class CrearMaquinaFormulario(forms.Form):
    # Valores de todos los productos
    marca = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    
    # Específicos Maquina
    nombre = forms.CharField(max_length=100)
    peso_limite = forms.IntegerField()
    instrucciones_de_uso = forms.CharField(max_length=500)
    
class CrearBarraFormulario(forms.Form):
    tipo_de_barra = (
        ('regular', 'Regular'),
        ('olimpica', 'Olimpica'),
    )
    # Valores de todos los productos
    marca = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    
    # Específicos Barra
    tipo = forms.ChoiceField(choices=tipo_de_barra)
    peso = forms.IntegerField()
    
class BusquedaMancuernaFormulario(forms.Form):
    peso = forms.IntegerField(required=False)
    
class BusquedaMaquinaFormulario(forms.Form):
    nombre = forms.CharField(max_length=100,required=False)
    
class BusquedaBarraFormulario(forms.Form):
    tipo_de_barra = (
        ('regular', 'Regular'),
        ('olimpica', 'Olimpica'),
    )
    tipo = forms.ChoiceField(choices=tipo_de_barra,required=False)