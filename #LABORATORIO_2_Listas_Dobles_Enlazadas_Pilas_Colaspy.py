#Laboratorio 2 - Daniel Castillo Jimenez - Cristofer Jarquin

import os

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def esta_vacia(self):
        return self.cabeza is None


    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo #ponemos la dirección del nuevo nodo en la cabeza de la lista, o sea al comienzo de la lista
            self.cola = nuevo_nodo # ponemos la dirección del nuevo nodo en la cola de la lista, o sea al final de la lista
        else:
            self.cola.siguiente = nuevo_nodo # El puntero siguiente del último nodo apunta al nuevo nodo
            nuevo_nodo.anterior = self.cola    # El puntero anterior del nuevo nodo apunta al último nodo
            self.cola = nuevo_nodo # El nuevo nodo se convierte en el último nodo de la lista
        self.tamaño += 1 # Incrementamos el tamaño de la lista en 1



    def insertar_medio(self, valor, posicion):

        #Verificar si la posición es válida
        if posicion < 0 or posicion > self.tamaño:
            raise IndexError("Posición fuera de rango")
            return

        #Si la posicion es 0, insertamos al inicio
        if posicion == 0:
            self.agregar_inicio(valor)
            return

        nuevo_nodo = Nodo(valor)
        actual = self.cabeza # Ponemos la variable temporal actual en la cabeza de la lista

        #Llegar al nodo qye actualmente ocupamos en la posición deseada
        for i in range(posicion):
            actual = actual.siguiente #avanza al siguiente nodo

            #conectar al nuevo nodo con el nodo anterior y el nodo siguiente
        nuevo_nodo.anterior = actual.anterior
        nuevo_nodo.siguiente = actual

        actual.anterior.siguiente = nuevo_nodo
        actual.anterior = nuevo_nodo

        self.tamaño += 1 # Incrementamos el tamaño de la lista en 1



    def eliminar_inicio(self):

        if(self.esta_vacia()):
            print("No se puede eliminar la lista está vacía.")
            return None

        valor_eliminado = self.cabeza.valor # Guardamos el valor del nodo que vamos a eliminar

        #Caso: Solamente existe un nodo

        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente # La cabeza apunta al siguiente nodo
            self.cabeza.anterior = None # El puntero anterior de la nueva cabeza es None
        self.tamaño -= 1 # Decrementamos el tamaño de la lista en 1
        return valor_eliminado # Retornamos el valor del nodo eliminado


    def eliminar_medio(self, posicion):
        if (self.esta_vacia()):
            print("No se puede eliminar la lista está vacía.")
            return None

        #Verificar si la posición es válida
        if posicion < 0 or posicion >= self.tamaño:
            raise IndexError("Posición fuera de rango")

        #Caso: Eliminar el primer nodo
        if posicion == 0:
            return self.eliminar_inicio()

        #Si es el ultimo elemento

        if posicion == self.tamaño - 1:
            return self.eliminarAlFinal()

        actual = self.cabeza

        #Buscar el nodo que desea eliminar

        for i in range(posicion):
            actual = actual.siguiente

        valor_eliminado = actual.valor # Guardamos el valor del nodo que vamos a eliminar

        #Guardar nodos anterior y siguiente

        anterior = actual.anterior
        siguiente = actual.siguiente

        #Reconectar los nodos

        anterior.siguiente = siguiente
        siguiente.anterior = anterior
        self.tamaño -= 1

        return valor_eliminado # Retornamos el valor del nodo eliminado

    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamaño += 1

    def recorrer_adelante(self):  # recorrerlo hacia la derecha -> puntero siguiente
        actual = self.cabeza
        while actual:  # actual == true
            print(actual.valor, end=" ")
            actual = actual.siguiente
        print("None")
    # recorrerlo hacia la izquierda -> puntero anterior

    def recorrer_atras(self):
        actual = self.cola
        while actual:  # is not None
            print(actual.valor, end=" ")
            actual = actual.anterior
        print("None")

    def buscar(self, valor):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1  # este elemento nunca estuvo en la lista doblemente enlazada.

    def tamaño_lista(self):
        return self.tamaño

    def eliminarAlFinal(self):
        if self.esta_vacia():
            print("No se puede eliminar la lista está vacía.")
            return None

        if self.cabeza == self.cola:  # Si solo hay un nodo en la lista
            valor_eliminado = self.cabeza.valor
            self.cabeza = None
            self.cola = None
            self.tamaño -= 1
            return valor_eliminado
        else:  # Hay más de un nodo, se elimina el último y se actualiza la cola
            valor_eliminado = self.cola.valor
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            self.tamaño -= 1
            return valor_eliminado
    def mostrarLista(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        actual = self.cabeza
        
        while actual:  # Mientras actual no sea None
            print(actual.valor, end=" <-> ")
            actual = actual.siguiente
        print("None")

# --- IMPLEMENTACIÓN PILA Y COLA ---
class Pila:
    def __init__(self): self.lista = ListaDoblementeEnlazada()
    def push(self, valor): self.lista.agregar_inicio(valor)
    def pop(self): return self.lista.eliminar_inicio()

class Cola:
    def __init__(self): self.lista = ListaDoblementeEnlazada()
    def enqueue(self, valor): self.lista.insertar_final(valor)
    def dequeue(self): return self.lista.eliminar_inicio()

if __name__ == "__main__":
    lista = ListaDoblementeEnlazada()
    pila = Pila()
    cola = Cola()

    while (True):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla
        print("\n --- MENU ---")
        print("0. Insertar final lista")
        print("1. Insertar en medio lista")
        print("2. Insertar al inicio lista")   
        print("3. La lista esta vacia.")
        print("4. Recorrer lista hacia adelante")
        print("5. Recorrer lista hacia atras")
        print("6. Buscar elemento en la lista")
        print("7. Tamaño de la lista")
        print("8. Eliminar al final de la lista")
        print("9. Eliminar al inicio de la lista")
        print("10. Eliminar al medio de la lista")
        print("11. Mostrar lista")
        print("12. Pila Push")
        print("13. Pila Pop")
        print("14. Cola Enqueue")
        print("15. Cola Dequeue")
        print("16. Salir")


        opcion = input("Elige una opcion: ")
        if (opcion == "0"):
            dato = input("Dato a insertar al final de la lista: ")
            lista.insertar_final(dato)
        elif (opcion == "1"):
            dato = input("Dato a insertar en el medio de la lista: ")
            posicion = int(input("Ingrese la posición para insertar en el medio: "))
            lista.insertar_medio(dato, posicion)
        elif (opcion == "2"):
            dato = input("Dato a insertar al inicio de la lista: ")
            lista.agregar_inicio(dato)
        elif (opcion=="3"):
            lista.esta_vacia()
        elif (opcion=="4"):
            lista.recorrer_adelante()
        elif (opcion=="5"):
            lista.recorrer_atras()
        elif (opcion=="6"):
            dato = input("Ingrese el elemento a buscar en la lista: ")
            posicion = lista.buscar(dato)
            if posicion != -1:
                print(f"Elemento encontrado en la posición: {posicion}")
            else:
                print("Elemento no encontrado en la lista.")
        elif (opcion=="7"):
            print(f"Tamaño de la lista: {lista.tamaño_lista()}")
        elif (opcion=="8"):
            print(f"Elemento eliminado del final: {lista.eliminarAlFinal()}")
        elif (opcion=="9"):
            print(f"Elemento eliminado del inicio: {lista.eliminar_inicio()}")
        elif (opcion=="10"):
            posicion = int(input("Ingrese la posición del elemento a eliminar: "))
            print(f"Elemento eliminado del medio: {lista.eliminar_medio(posicion)}")
        elif (opcion=="11"):
            lista.mostrarLista()
        elif (opcion=="12"):
            pila.push(input("Dato Push Pila: "))
        elif (opcion=="13"):
            print(f"Pop Pila: {pila.pop()}")
        elif (opcion=="14"):
            cola.enqueue(input("Dato Enqueue Cola: "))
        elif (opcion=="15"):
            print(f"Dequeue Cola: {cola.dequeue()}")
        elif (opcion=="16"):
            print("Saliendo del programa...")
            break
        
        input("\nPresiona Enter para continuar...")


















