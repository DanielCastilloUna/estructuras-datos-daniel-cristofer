# 1Crear una lista doblemente enlazada de productos de un supermercado

#2Caracteristicas: id, nombre, precio, pais de origen, existencias.

#3Generar un menu: Ingresar productos, eliminar productos, buscar productos, lo haremos por nombre

#4Funcion que permita pasar los productos de la lista doble que esten en cero existencias a una cola
#con el objetivo que se tenga una lista de compras de suministros para el supermercado

#5Genere una lista de frecuencias con los paises para saber de que lugar es donde se esta importando mas productos

#6Generar un reporte archivo.txt de lo que debe recuperar el supermercado el dia de hoy.

# 7-> Para el punto anterior, realizar una suma de la cantidad  de cada producto por su precio

# 8-> Realizar un metodo recursivo que muestre la lista doblemente enlada

# 

import os

class Nodo:
    def __init__(self,id,nombre,precio,pais,existencias):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.pais = pais
        self.existencias = existencias
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamannio = 0
        

    def esta_vacia(self):
        return None

    def insertar(self,id,nombre,precio,pais,existencias): # Lo hace al inicio de la lista
        nuevo_nodo = Nodo(id,nombre,precio,pais,existencias)
        if self.esta_Vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamannio +=1 # Nodos / Productos totales en el catalogo
        

    def eliminar(self): # Lo hace del final de la lista

        if self.esta_vacia():
            print("No se puede eliminar, la lista esta vacia")
            return None
        else:
            valor_eliminado = self.cola.dato
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            self.tamannio -=1
            
            return valor_eliminado

    def menu_super(lista_super): # Ingresar, eliminar y buscar juntos

        
        while(True):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n --- MENU ---")
            print("0. Insertar producto")
            print("1. Buscar producto")
            print("2. Eliminar producto")   
            print("3. Salir")

            opcion = input("Elige una opcion: ")
            if (opcion == "0"):
                #Pedimos los 5 atributos
                id_prod = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                pais = input("País de origen: ")
                existencias = int(input("Existencias: "))



                producto =input("Producto a insertar: ")
                lista_super.insertar(id_prod, nombre, precio, pais, existencias)

            elif (opcion == "1"):
                nombre_buscar =input("Producto a buscar: ")
                lista_super.buscarElemento(nombre_buscar)
            
            elif (opcion == "2"):
                nombre_eliminar =input("Producto a eliminar: ")
                lista_super.eliminar(nombre_eliminar)  
            elif (opcion=="3"):
                print("Saliendo del programa...")
                break  
            input("\nPresiona Enter para continuar...")
            



    def buscarElemento(self,nombre_referencia):

        if self.esta_Vacia():
            print("La lista esta vacia, no hay nada para buscar")
            return None
        actual = self.cabeza
        while(actual!= None and actual.dato != nombre_referencia):
            actual = actual.siguiente
        if(actual!= None):
            print(f"Producto'{nombre_referencia}' fue encontrado con exito")
            print(f"Existencias del producto: '{self.existencias}'\n")
            return actual.dato
        else:
            print(f"Producto'{nombre_referencia}' no fue encontrado.")
            return None


    def aumentar_reponer_stock(self,nombre_producto,cantidad):
        actual = self.cabeza
        while(actual is not None):
            if(actual.nombre == nombre_producto):
                actual.existencias += cantidad
                print(f"Nuevo stock de {actual.nombre}: {actual.existencias}")
                return
            actual = actual.siguiente
        print("Producto no encontrado")





    def encolar_productos_agotados(lista_super):
        cola_compras = ListaDoblementeEnlazada()
        actual = lista_super.cabeza

        while actual != None:
            if(actual.existencias ==0):
                cola_compras.insertar(actual.id,actual.nombre,actual.precio,actual.pais,actual.existencias)
                print(f"Producto encolado -> {actual.nombre}")
            actual = actual.siguiente
        return cola_compras
            


            
            
    