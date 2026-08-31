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
    def __init__(self, id, nombre, precio, pais, existencias):
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
        return self.cabeza is None  # Corregido: antes retornaba None

    def insertar(self, id, nombre, precio, pais, existencias): # Lo hace al inicio de la lista
        nuevo_nodo = Nodo(id, nombre, precio, pais, existencias)
        if self.esta_vacia():  # Corregido: ajustado a minúscula
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamannio += 1 # Nodos / Productos totales en el catalogo

    def eliminar(self, nombre_referencia=None): # Lo hace del final o por nombre según se requiera
        if self.esta_vacia():
            print("No se puede eliminar, la lista esta vacia")
            return None
        
        # Si se pasa nombre_referencia, busca y elimina ese nodo
        if nombre_referencia:
            actual = self.cabeza
            while actual is not None and actual.nombre.lower() != nombre_referencia.lower():
                actual = actual.siguiente

            if actual is None:
                print(f"Producto '{nombre_referencia}' no fue encontrado para eliminar.")
                return None

            if self.cabeza == self.cola:
                self.cabeza = None
                self.cola = None
            elif actual == self.cabeza:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
            elif actual == self.cola:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
            else:
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior

            self.tamannio -= 1
            print(f"Producto '{actual.nombre}' eliminado con exito.")
            return actual.nombre
        else:
            # Lógica original del final por si se usa sin parámetro
            valor_eliminado = self.cola.nombre if self.cola else None
            if self.cabeza == self.cola:
                self.cabeza = None
                self.cola = None
            else:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
            self.tamannio -= 1
            return valor_eliminado

    def menu_super(lista_super):
        while(True):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n --- MENU SUPERMERCADO ---")
            print("0. Insertar producto")
            print("1. Buscar producto")
            print("2. Eliminar producto")   
            print("3. Ver lista completa (Recursivo)")
            print("4. Ver frecuencia de paises")
            print("5. Generar reporte de recuperacion (.txt)")
            print("6. Salir")

            opcion = input("Elige una opcion: ")
            if (opcion == "0"):
                id_prod = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                pais = input("País de origen: ")
                existencias = int(input("Existencias: "))
                lista_super.insertar(id_prod, nombre, precio, pais, existencias)
                print("Producto insertado con exito.")

            elif (opcion == "1"):
                nombre_buscar = input("Producto a buscar: ")
                lista_super.buscarElemento(nombre_buscar)
            
            elif (opcion == "2"):
                nombre_eliminar = input("Producto a eliminar: ")
                lista_super.eliminar(nombre_eliminar)

            elif (opcion == "3"):
                lista_super.imprimir_lista_recursiva()

            elif (opcion == "4"):
                lista_super.frecuencia_paises()

            elif (opcion == "5"):
                lista_super.generar_reporte_recuperacion()

            elif (opcion == "6"):
                print("Saliendo del programa...")
                break   
            input("\nPresiona Enter para continuar...")
            
    def buscarElemento(self, nombre_referencia):
        if self.esta_vacia():
            print("La lista esta vacia, no hay nada para buscar")
            return None
        actual = self.cabeza
        while(actual != None and actual.nombre.lower() != nombre_referencia.lower()):
            actual = actual.siguiente
        if(actual != None):
            print(f"Producto '{nombre_referencia}' fue encontrado con exito")
            print(f"Existencias del producto: '{actual.existencias}'\n")  # Corregido: antes decía self.existencias
            return actual.nombre
        else:
            print(f"Producto '{nombre_referencia}' no fue encontrado.")
            return None

    def aumentar_reponer_stock(self, nombre_producto, cantidad):
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
            if(actual.existencias == 0):
                cola_compras.insertar(actual.id, actual.nombre, actual.precio, actual.pais, actual.existencias)
                print(f"Producto encolado -> {actual.nombre}")
            actual = actual.siguiente
        return cola_compras
        
        #5 lista de frecuencias con los paises
        def frecuencia_paises(self):
        if self.esta_vacia():
            print("La lista esta vacia, no hay paises que registrar.")
            return
        
        frecuencias = {}
        actual = self.cabeza
        while actual is not None:
            pais = actual.pais.strip().capitalize()
            frecuencias[pais] = frecuencias.get(pais, 0) + 1
            actual = actual.siguiente

        print("\n--- LISTA DE FRECUENCIAS DE PAISES (IMPORTACIONES) ---")
        paises_ordenados = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
        for pais, freq in paises_ordenados:
            print(f"Pais: {pais} -> {freq} producto(s) importado(s)")
        
        lugar_mayor = paises_ordenados[0][0]
        print(f"\nEl pais desde donde se esta importando mas es: {lugar_mayor}")

        #Reporte .txt y cálculo de recuperación
        def generar_reporte_recuperacion(self, nombre_archivo="reporte_recuperacion.txt"):
        if self.esta_vacia():
            print("La lista esta vacia, no hay productos para generar reporte.")
            return

        cola_agotados = self.encolar_productos_agotados()
        if cola_agotados.esta_vacia():
            print("\nNo hay productos con 0 existencias hoy. El reporte saldra vacio.")
            
        total_inversion = 0
        lineas_reporte = []
        lineas_reporte.append("==================================================")
        lineas_reporte.append("   REPORTE DIARIO DE SUMINISTROS A RECUPERAR      ")
        lineas_reporte.append("==================================================\n")

        actual = cola_agotados.cabeza
        while actual is not None:
            cantidad_a_pedir = 10  # Lote estimado para reponer stock agotado
            subtotal = cantidad_a_pedir * actual.precio
            total_inversion += subtotal

            lineas_reporte.append(f"ID: {actual.id} | Producto: {actual.nombre} | Pais: {actual.pais}")
            lineas_reporte.append(f"  -> Precio Unitario: {actual.precio} | Cantidad a pedir: {cantidad_a_pedir}")
            lineas_reporte.append(f"  -> Subtotal a invertir: {subtotal}\n")
            actual = actual.siguiente

        lineas_reporte.append("--------------------------------------------------")
        lineas_reporte.append(f"MONTO TOTAL NECESARIO PARA RECUPERAR HOY: {total_inversion}")
        lineas_reporte.append("==================================================")

        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("\n".join(lineas_reporte))

        print(f"\nReporte generado exitosamente con el nombre: '{nombre_archivo}'")
        print(f"Monto total de recuperacion calculado: {total_inversion}")

        # método recursivo que muestre la lista doblemente enlada
        def mostrar_recursivo(self, nodo_actual):
        if nodo_actual is None:
            return
        print(f"ID: {nodo_actual.id} | Nombre: {nodo_actual.nombre} | Precio: {nodo_actual.precio} | Pais: {nodo_actual.pais} | Existencias: {nodo_actual.existencias}")
        self.mostrar_recursivo(nodo_actual.siguiente)

    def imprimir_lista_recursiva(self):
        if self.esta_vacia():
            print("La lista esta vacia.")
        else:
            print("\n--- MOSTRANDO LISTA DOBLEMENTE ENLAZADA (RECURSIVO) ---")
            self.mostrar_recursivo(self.cabeza)
     


            
            
    
