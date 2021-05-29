# Denavith para resolver cinematica directa.

Denavith es una libreria de uso libre que permite resolver matrices de rotacion por el metodo **Denavith-Hartengberg** utilizando Notebooks.

El metodo esta basado en el libro *Fundamentos de Robótica
Antonio Barrientos Cruz · Mcgraw-Hill / Interamericana De España, S.A.*

  - Crea modelos roboticos de cinematica directa utilizando calculos simbolicos.
  - Resuelve modelos roboticos de cinematica directa.

###	Consideraciones
En la libraria se hace referencia en especial a cuatro parametros *(theta, d, a, alpha).* estos hacen referencia a:

-	**theta** = angulo de rotacion para la 'n-esima' articulacion en el eje Z.	(rotacion en z).
-	**d** = movimiento del punto de referencia a travez del eje Z. (Traslacion en z).
-	**a** = movimiento del punto de referencia a travez del eje X. (Traslacion en x).
-	**alpha** = angulo de rotacion para la 'n-esima' articulacion en el eje X.(rotacion en x).



###	Como utilizarlo


**NOTA : Es importante que sepas que para agregar angulos debes hacerlo en radianes, es decir:**

**-	pi = 180°**
**-	pi / 2 = 90°**
**-	2 pi = 360°**


1. Importa la libreria en tu proyeto.

```python
import denavith 
```

2. Crea las variables simbolicas necesarias.

```python
#Declara las variables simbolicas de esta manera.
q1,q2,q3,l1 = dh.simbolic('q1 q2 q3 l1')

#Imprimimos las variables declaradas.
q1,q2,q3,l1
```
3. Crea un modelo por cada robot que desees evaluar.

```python
#Creamos un objeto para el robot de este modelo
robot_tipo1 = dh.robot()

#Crea y evalua mas de un tipo de robot a la vez.
robot_tipo2 = dh.robot()
```

4. Agrega articulaciones al objeto del modelo.

```python
#Robot 1.

#articulacion 0.
robot_tipo1.add_articulation(q1 , l1, 0, dh.pi/2)

#articulacion 1.
robot_tipo1.add_articulation(q2 , 0, 0, -dh.pi/2)

#articulacion 2.
robot_tipo1.add_articulation(0 ,q3,0,0)

#NOTA:
#Puedes obtener el valor de Pi directamente de la libreria.
```

5. Resuelve la matriz de rotacion.

```python
#Mostramos el resultado.
robot_tipo1.solve()
```

## Funciones.


|Nombre de la funcion | Descripcion          |
| ------------- | ------------------------------ |
| `simbolic()`      | Regresa las variables simbolicas establecidas a travez de una cadena de texto.       |
| `robot()`   | Crea un nuevo objeto que posee las funciones necesarias para el analisis matematico.    |

### Funciones del objeto robot(). 

|Nombre de la funcion | Descripcion          |
| ------------- | ------------------------------ |
| `robot.add_articulation(theta, d, a, alpha)`      | Agrega una matriz de Denavit-Hartengber en 'articulation_array', para la articulacion 'n', esta se agrega a un array que guarda las matrices de 'n' articulacion, 'articulation_array' es un arreglo que contiene las matrices de cada articulacion.       |
| `robot().get_articulation_array()`   | Imprime la matriz 'articulation_array', que es un arreglo con las matrices generadas para 'n' articulacion, el orden es de la mas antigua a la mas reciente.  |
| `robot().reset_articulation_array()`   |  Resetea y deja vacio el arreglo que contiene las matrices de cada articulacion.  |
| `robot().solve()`   |  Regresa la matriz resultado de Denavit Hartenberg.        El retorno de un valor 1, es tomado como error dado que no se ha procesado la informacion. |

------------
