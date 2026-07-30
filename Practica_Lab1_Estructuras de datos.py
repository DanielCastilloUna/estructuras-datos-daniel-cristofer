


 #Laboratorio 1 Estructuras de Datos / Daniel Castillo Jimenez / Cristofer Jarquin Gutierrez

#Insertar al inicio de una lista simplemente enlazada, insertar normal, e insertar al medio


import os #importe la libreria os para limpiar la pantalla en el menu


# 1 Creacion de la clase nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    #Ahora nos preguntamos como insertar un nodo al inicio de la lista, para ello crearemos un metodo llamado insertar_al_inicio
    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato) #creamos a la persona nueva
        nuevo_nodo.siguiente = self.cabeza #agarra a la persona que esta a la derecha y la pone a la izquierda de la nueva persona
        self.cabeza = nuevo_nodo # la direccion de la persona anterior ahora apunta a la nueva persona

    def insertar_al_medio(self,dato,dato_referencia):
        nuevo_nodo = Nodo(dato)
        current = self.cabeza 
        while(current != None and current.dato != dato_referencia):
            current = current.siguiente #avanzamos al siguiente nodo
        if(current!= None):
            nuevo_nodo.siguiente = current.siguiente # guardamos la direccion del siguiente nodo en el nuevo nodo
            current.siguiente = nuevo_nodo # actualizamos la direccion del nodo actual para que apunte al nuevo nodo
        else:
            print("Dato de referencia no fue encontrado")

    def insertar(self,dato):
        new_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = new_nodo
            return
        current = self.cabeza
        while (current.siguiente):
            current = current.siguiente
        current.siguiente = new_nodo


    def display(self):
        current = self.cabeza
        if(current==None):
            print("La lista esta vacia")
            return
        while (current):
            print(current.dato, end=" -> ")
            current = current.siguiente
        print("Fin de la lista")



    #Eliminacion de nodos de una lista enlazada

    def _eliminate__in_position(self,posicion):

        #Verificar si la lista esta vacia
        if self.cabeza is None:
            print("La lista esta vacia")
            return
        #Eliminar el primer nodo, determinar si existe una lista vacia, buscar un elemento dentro de la lista, generar un menu con todas las opciones
        if (posicion == 0):
            self.cabeza = self.cabeza.siguiente #Mueve la cabeza al siguiente nodo, eliminando el primer nodo
            return
        actual = self.cabeza #Colocamos una variable temporal para recorrer la lista
        contador = 0

        #Buscar el nodo anterior a la posicion
        while (actual.siguiente is not None and contador < posicion - 1):
            actual = actual.siguiente #Avanzamos al siguiente nodo
            contador += 1 #incrementamos el contador
        #verificar si la posicion es valida
        if (actual.siguiente is None):
            print("Posicion fuera de rango")
            return
        #saltar al nodo que se desea eliminar
        actual.siguiente = actual.siguiente.siguiente #Elimina el nodo al saltar la referencia del nodo a eliminar
        
    def _eliminar_al_Inicio_(self):

        #verificar si la lista esta vacia
        if(self.cabeza is None):
            print("La lista esta vacia")
            return
        self.cabeza = self.cabeza.siguiente #Mueve la cabeza al siguiente nodo, eliminando el primer nodo
    def _que_Hace(self): #elimina el ultimo elemento de la lista enlazada

        #Verifica si la lista esta vacia
        if self.cabeza is None:
            print("La lista esta vacia")
            return #habia error de indentacion, ya corregido

        if (self.cabeza.siguiente is None): #si no hay ningun nodo adelante
            self.cabeza = None #La lista esta vacia, entonces el inicio de la lista queda apuntando a None
            return

        actual = self.cabeza
        while(actual.siguiente.siguiente): #avanza al nodo que esta por delante del que esta apuntando, hasta que apunte a None
            actual = actual.siguiente

        actual.siguiente = None


    #Determinar si existe una lista vacia

    def _listaVacia_(self):
        #Simplemente verifica si la lista esta vacia y devuelve un mensaje

        if(self.cabeza is None):
            print("La lista esta vacia.")
            return True
        else:
            print("La lista no esta vacia.")
            return False

    def _buscar_Elemento_Lista(self,dato_referencia):

        current = self.cabeza
        while(current != None and current.dato != dato_referencia):
            current = current.siguiente       
        if(current!=None):
            print("Elemento encontrado.")
            return current.dato
        else:
            print("El elemento no existe en la lista")
            return None
def menu():
        lista =  ListaEnlazada()

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla para Windows y Linux/Mac
            print("\n --- MENU ---")
            print("0. Mostrar lista")
            print("1.Insertar al inicio")
            print("2.Insertar al medio")
            print("3. Insertar al final")
            print("4. Eliminar al final")
            print("5. Eliminar en una posicion")
            print("6.Eliminar al inicio")
            print("7. Verificar si la lista esta vacia")
            print("8. Buscar un elemento de la lista")
            print("9. Salir")

            opcion = input("Elige una opcion: ")
            if(opcion=="0"):
                print("Display de la lista")
                lista.display()
            elif(opcion=="1"):
                dato = input("Dato a insertar al inicio de la lista: ")
                lista.insertar_al_inicio(dato)
            elif (opcion=="2"):
                dato = input("Dato a insertar en el medio de la lista: ")
                dato_referencia = input("Ingrese el dato de referencia para insertar al medio: ")
                lista.insertar_al_medio(dato, dato_referencia)
            elif (opcion=="3"):
                dato = input("Dato a insertar al final de la lista: ")
                lista.insertar(dato)
            elif(opcion=="4"):
                print("Eliminar el ultimo elemento de la lista")
                lista._que_Hace()
            elif(opcion=="5"):
                    try:
                        pos = int(input("Ingrese la posición del elemento a eliminar: "))
                        lista._eliminate__in_position(pos)
                    except ValueError:
                        print("Debes ingresar un número válido")
            elif(opcion=="6"):
                lista._eliminar_al_Inicio_()
            elif(opcion=="7"):
                print("Verificar si la lista esta vacia")
                lista._listaVacia_()
            elif(opcion=="8"):
                dato = input("Buscar elemento de la lista: ")
                lista._buscar_Elemento_Lista(dato)
            elif(opcion=="9"):
                print("Salio del programa exitosamente")
                break
            else:
                print("Opcion no valida")

            input("\nPresiona Enter para continuar...")


menu()


