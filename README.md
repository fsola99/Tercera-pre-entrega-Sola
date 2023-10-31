# Tercera-pre-entrega-Sola
Tercera pre-entrega para curso de Python en Coderhouse hecha por Federico Sola.

## ¿De qué trata mi trabajo?
La web simula una tienda de Instrumentos para el Gimnasio. Existen 4 (3 disponibles) modelos:
- Producto: de éste heredan los tres modelos aplicados. Tiene dos atributos:
    - Precio Integer.
    - Marca: Char (max_length=50).
- Mancuernas: hereda de producto los atributos mencionados. Tiene un atributo adicional:
    - Peso: Integer.
- Máquinas: hereda de producto los atributos mencionados. Tiene tres atributos adicionales:
    - Nombre: Char (max_length=100).
    - Peso límite: Integer.
    - Instrucciones de uso: Text (max_length=500).
- Barras: hereda de producto los atributos mencionados. Tiene dos atributos adicionales:
    - Tipo: Char (max_length=25,choices=tipo_de_barra); los tipos de barra pueden ser regular u olímpica.
    - Peso: Integer.

## ¿Qué se puede hacer en él?
1) Crear cualquier cantidad de los tres diferentes modelos de instrumentos para el gimnasio previamente mencionados.
2) Ver los productos creados.
3) Filtrar/buscar sobre la lista total de cada uno de ellos según un filtro específico:
    - Mancuerna: peso.
    - Maquina: nombre (o que lo contenga).
    - Barra: tipo.

## ¿Cómo lo probaría?
1) Crear varias instancias de cada clase de productos, usando valores diferentes en los atributos "filtro".
2) Realizar búsquedas para probar el correcto funcionamiento.

## ¿Dónde están las funcionalidades?
- index: Página de inicio.
- 'mancuernas/': listado de mancuernas, más función de búsqueda de mancuernas según un peso indicado.
- 'maquinas/': llistado de máquinas, más función de búsqueda de máquinas que contenga un nombre indicado.
- 'barras/': listado de barras, más función de búsqueda de barras según un tipo de barra (regular u olímpica) indicado.
- 'mancuernas/crear/': creación de mancuernas.
- 'maquinas/crear/': creación de maquinas.
- 'barras/crear/': creación de barras.
