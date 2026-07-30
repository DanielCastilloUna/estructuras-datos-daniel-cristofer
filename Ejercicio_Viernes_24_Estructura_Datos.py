from platform import node



#Sigue una estructura


class Node:
    def __init__(self, valor):
        self.data = valor # el contenido del nodo en ese momento
        self.next = None # inicializo el puntero siguiente en null / None = null
#fin de la clase nodo

#Creacion de la lista
class SimpleList:
    
    def __init__(self):
        self.head = None # inicializo la cabeza de la lista en null / None = null


    def insert(self,valor):
        new_node= Node(valor) # creo un nuevo nodo con el valor que me pasan
        if (self.head is None):
            self.head = new_node # si la cabeza es null, el nuevo nodo se convierte en la cabeza
            return
        current = self.head # si la cabeza no es null, creo un nodo temporal que apunta a la cabeza
        while (current.next): # mientras el siguiente nodo no sea null
            current = current.next
        current.next = new_node # cuando el siguiente nodo sea null, el nuevo nodo se convierte en el siguiente nodo del nodo temporal
      
    def display(self):
        current = self.head # creo un nodo temporal que apunta a la cabeza
        while (current): # mientras el nodo temporal no sea null
            print(current.data, end= " ->   ") # imprimo el valor del nodo temporal
            current = current.next # muevo el nodo temporal al siguiente nodo
        print("Fin de la lista") # cuando el nodo temporal sea null, imprimo que es el fin de la lista

lista1 = SimpleList() # creo una lista vacia
lista1.insert(10) # inserto el valor 10 en la lista
lista1.insert(20) # inserto el valor 20 en la lista
lista1.insert(30) # inserto el valor 30 en la lista
lista1.display() # muestro los valores de la lista

#practicar insertar al final,eliminar un elemento, insertar al inicio(PRIORIDAD), insertar al medio(PRIORIDAD), buscar un elemento especifico, la proxima semana tenemos el primer laboratorio que vale 8% el martes
#despues subir la respuesta a nuestro repositorio de github y enviar el link al profesor