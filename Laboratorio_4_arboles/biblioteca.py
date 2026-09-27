# LABORATORIO 4 - ÁRBOLES BINARIOS DE BÚSQUEDA (Biblioteca)
# Integrantes: Cristofer Jarquín, Daniel Castillo

# ---------- Paso 0: comprobar que se abren los dos archivos ----------
with open('catalogo_libros.txt', encoding='utf-8') as archivo:
    print('Primer libro:', archivo.readline().strip())
with open('movimientos.txt', encoding='utf-8') as archivo:
    print('Primer movimiento:', archivo.readline().strip())