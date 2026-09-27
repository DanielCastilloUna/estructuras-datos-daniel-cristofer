# LABORATORIO 4 - ÁRBOLES BINARIOS DE BÚSQUEDA (Biblioteca)
# Integrantes: Cristofer Jarquín, Daniel Castillo

# ---------- Paso 0: comprobar que se abren los dos archivos ----------
with open('catalogo_libros.txt', encoding='utf-8') as archivo:
    print('Primer libro:', archivo.readline().strip())
with open('movimientos.txt', encoding='utf-8') as archivo:
    print('Primer movimiento:', archivo.readline().strip())



# ---------- Paso 1: nodo y construcción del árbol ----------
class NodoLibro:
    def __init__(self, codigo, titulo, disponibles):
        self.codigo = codigo
        self.titulo = titulo
        self.disponibles = disponibles
        self.izquierdo = None
        self.derecho = None


def insertar(raiz, codigo, titulo, disponibles):
    if raiz is None:
        return NodoLibro(codigo, titulo, disponibles)
    if codigo < raiz.codigo:
        raiz.izquierdo = insertar(raiz.izquierdo, codigo, titulo, disponibles)
    elif codigo > raiz.codigo:
        raiz.derecho = insertar(raiz.derecho, codigo, titulo, disponibles)
    else:
        raise ValueError(f'Código duplicado: {codigo}')
    return raiz


def cargar_catalogo(ruta):
    raiz = None
    with open(ruta, encoding='utf-8') as archivo:
        for numero, linea in enumerate(archivo, 1):
            if not linea.strip():
                continue
            partes = linea.strip().split('|')
            if len(partes) != 3:
                raise ValueError(f'Línea {numero} incorrecta')
            codigo, titulo, disponibles = partes
            if int(disponibles) < 0:
                raise ValueError(f'Inventario negativo en línea {numero}')
            raiz = insertar(raiz, int(codigo), titulo, int(disponibles))
    return raiz


raiz = cargar_catalogo('catalogo_libros.txt')
print('Raíz:', raiz.codigo)  # 410
print('Hijos de 260:', raiz.izquierdo.izquierdo.codigo, 'y', raiz.izquierdo.derecho.codigo)
print('Hijos de 580:', raiz.derecho.izquierdo.codigo, 'y', raiz.derecho.derecho.codigo)



# ---------- Paso 2: consultar el catálogo ----------
def buscar(nodo, codigo):
    if nodo is None or nodo.codigo == codigo:
        return nodo
    if codigo < nodo.codigo:
        return buscar(nodo.izquierdo, codigo)
    return buscar(nodo.derecho, codigo)


def listado_inorden(nodo):
    if nodo is None:
        return []
    return (listado_inorden(nodo.izquierdo)
            + [(nodo.codigo, nodo.titulo, nodo.disponibles)]
            + listado_inorden(nodo.derecho))


print('Libro 330:', buscar(raiz, 330).titulo)
print('Código 999 registrado:', buscar(raiz, 999) is not None)
for libro in listado_inorden(raiz):
    print(libro)