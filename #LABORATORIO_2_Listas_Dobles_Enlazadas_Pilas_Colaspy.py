#Laboratorio 2 - Daniel Castillo Jimenez - Cristofer Jarquin



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
            self.cabeza = nuevo_nodo 
            self.cola = nuevo_nodo 
        else:
            self.cola.siguiente = nuevo_nodo 
            nuevo_nodo.anterior = self.cola    
            self.cola = nuevo_nodo 
        self.tamaño += 1 

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

    def recorrer_adelante(self):  
        actual = self.cabeza
        while actual:  
            print(actual.valor, end=" ")
            actual = actual.siguiente
        print("None")

    def tamaño_lista(self):
        return self.tamaño

    def cantidadElementos(self):
        return self.tamaño

    def obtenerMayor(self):
        if self.esta_vacia():
            return None
        actual = self.cabeza
        mayor = actual.valor
        while actual:
            if actual.valor > mayor:
                mayor = actual.valor
            actual = actual.siguiente
        return mayor

    def obtenerMenor(self):
        if self.esta_vacia():
            return None
        actual = self.cabeza
        menor = actual.valor
        while actual:
            if actual.valor < menor:
                menor = actual.valor
            actual = actual.siguiente
        return menor

    def obtenerPromedio(self):
        if self.esta_vacia():
            return 0
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma / self.tamaño


if __name__ == "__main__":
    lista = ListaDoblementeEnlazada()

    try:
        with open("datos.txt","r") as archivo:
            for linea in archivo:
                linea = linea.strip()  
                if linea!= "":
                    valor = int(linea)
                    lista.agregar_inicio(valor)

    except FileNotFoundError:
        print("Error: el archivo datos.txt no se encontró.")
        exit()

    except ValueError:
        print("Error: el archivo datos.txt contiene un valor no válido.")
        exit()

    # Generación exclusiva del reporte
    with open("Reporte.txt", "w") as archivo:
        archivo.write("====================================\n")
        archivo.write("    REPORTE DE TEMPERATURAS\n")
        archivo.write("====================================\n\n")
        archivo.write(f"Cantidad de temperaturas: {lista.cantidadElementos()}\n")
        archivo.write(f"Temperatura mayor: {lista.obtenerMayor()}\n")
        archivo.write(f"Temperatura menor: {lista.obtenerMenor()}\n")
        archivo.write(f"Temperatura promedio: {lista.obtenerPromedio():.2f}\n\n")
        archivo.write("Integrantes: Daniel Castillo Jimenez - Cristofer Jarquin\n")

    print("¡Reporte generado con éxito en 'Reporte.txt'!")






















