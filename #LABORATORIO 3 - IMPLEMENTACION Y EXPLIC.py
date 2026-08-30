#LABORATORIO 3 - IMPLEMENTACION Y EXPLICACION DE ALGORITMO DE ORDENAMIENTO QUICKSORT
#Ejercicio asignado: Quick Sort
#Estudiantes: Daniel Castillo Jimenez - Cristofer Jarquin Gutierrez

import random # Importamos la libreria random para generar numeros aleatorios
import time # Importamos la libreria time para medir el tiempo de ejecucion del algoritmo



#Parte 1 - Setup | Generacion de datos aleatorios

random.seed(42) # Semilla para reproducibilidad del recorrido manual

datos = [random.randint(1, 100) for _ in range(20)] # Generamos una lista de 10 numeros aleatorios entre 1 y 100
print("Datos aleatorios generados:", datos) # Imprimimos los datos generados

#Parte VI - Quick Sort (pivote = ultimo elemento)

def quicksort_ultimo(lista, nivel =0, mostrar = False):

    if(len(lista) <= 1): # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
        return lista
    pivote = lista[-1] # Elegimos el último elemento como pivote
    menores = [x for x in lista[:-1] if x <= pivote] # Lista para elementos menores que el pivote
    mayores = [x for x in lista[:-1] if x > pivote] # Lista para elementos mayores o iguales al pivote

    if mostrar: # Si se desea mostrar el proceso de ordenamiento
        print(f"Nivel {nivel}: Pivote = {pivote}, Menores = {menores}, Mayores = {mayores}")
        return (quicksort_ultimo(menores, nivel + 1, mostrar) + [pivote] + quicksort_ultimo(mayores, nivel + 1, mostrar))


def quicksort_primero(lista): # Quick Sort - pivote = primer elemento         
    if len(lista) <= 1: # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
        return lista
    pivote = lista[0] # Elegimos el primer elemento como pivote
    menores = [x for x in lista[1:] if x <= pivote] # Lista para elementos menores que el pivote
    mayores = [x for x in lista[1:] if x > pivote] # 
    return quicksort_primero(menores) + [pivote] + quicksort_primero(mayores) # Retornamos la lista ordenada

def quicksort_centro(lista): # Quick Sort - pivote = elemento del centro
    if len (lista) <= 1: # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
        return lista
    centro = len(lista) // 2 # Calculamos el índice del elemento central
    pivote = lista[centro] # Elegimos el elemento central como pivote
    resto = lista[:centro] + lista[centro + 1:] # Creamos una lista sin el pivote
    menores = [x for x in resto if x <= pivote] # Lista para elementos menores que el pivote
    mayores = [x for x in resto if x > pivote] # Lista para elementos mayores que el pivote
    return quicksort_centro(menores) + [pivote] + quicksort_centro(mayores) # Retornamos la lista ordenada



# lista_ordenada = list(range(500))
# print("Intentando ordenar una lista ya ordenada de 1000 elementos")
# print("Elegimos el pivote como ultimo elemento, y no le aumentamos a python el limite de recursion")
# resultado = quicksort_ultimo(lista_ordenada,mostrar=True)
# print("Esto no se va a imprimir", resultado[:10]) #No se imprime cuando alcanza el limite de llamadas





print("\n" + "=" * 60)
print("RECORRIDO MANUAL - Quick Sort con [10, 7, 8, 9, 1, 5]")
print("Pivote = Ultimo elemento")
print("=" * 60)
lista_prueba = [10, 7, 8, 9, 1, 5]
resultado = quicksort_ultimo(lista_prueba.copy(), mostrar=True)
print(f"\nLista ordenada: {resultado}")

print("\nComparacion con pivote = primer elemento:")
print(quicksort_primero(lista_prueba.copy()))

print("\nComparacion con pivote = elemento del centro:")
print(quicksort_centro(lista_prueba.copy()))




#Parte VIII - Medición de tiempo de ejecución

def medir(lista):
    copia = lista.copy() # Hacemos una copia de la lista para no modificar la original
    inicio = time.perf_counter() # Iniciamos el contador de tiempo
    quicksort_ultimo(copia) # Ejecutamos el algoritmo de Quick Sort
    fin = time.perf_counter() # Detenemos el contador de tiempo
    return fin - inicio # Retornamos el tiempo transcurrido

print("\n" + "=" * 70)
print("Parte VIII - Medición de tiempos con distintos tamaños Quick Sort")
print("=" * 70)
print(f"{'Tamannio':<10}{'Aleatorio':<18}{'Ordenada':<18}{'Invertida':<18}")

for n in [100,500,1000,5000]: #Probamos tammanios de 100, 500, de 1000 y 5000
    aleatoria = [random.randint(1, 1000000) for _ in range(n)] # Generamos una lista aleatoria de tamaño n
    ordenada = list(range(n))
    invertida = list(range(n, 0, -1)) # Generamos una lista invertida de tamaño n
    t_aleatoria = medir(aleatoria) # Medimos el tiempo de ejecución para la lista aleatoria
    t_ordenada = medir(ordenada) # Medimos el tiempo de ejecución para la lista ordenada
    t_invertida = medir(invertida) # Medimos el tiempo de ejecución para la lista invertida
    print(f"{n:<10}{t_aleatoria:<18.6f}{t_ordenada:<18.6f}{t_invertida:<18.6f}") # Imprimimos los resultados

#Parte IX - Diferentes condiciones de entrada (n = 1000)

print("\n" + "=" * 70)
print("Parte IX - Diferentes condiciones de entrada (n = 1000)")
print("="*70)
caso_a = random.sample(range(1,10000),1000)
caso_b = list(range(1000))
caso_c = list(range(1000,0,-1))

t_a = medir(caso_a)
t_b = medir(caso_b)
t_c = medir(caso_c)
print(f"{'Algoritmo':<15}{'Aleatoria':<15}{'Ordenada':<15}{'Invertida':<15}")
print(f"{'Quick Sort':<15}{t_a:15.6f}{t_b:15.6f}{t_c:15.6f}")
