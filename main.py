from gestor_biblioteca.ArticuloCientifico import *
from gestor_biblioteca.Autor import *
from gestor_biblioteca.Categoria import *
from gestor_biblioteca.Copia import *
from gestor_biblioteca.Lector import *
from gestor_biblioteca.Libro import *
from gestor_biblioteca.Multa import *
from gestor_biblioteca.Prestamo import *
from gestor_biblioteca.Tesis import *
from gestor_biblioteca.share import *

"""
FALTANTES
- Tildes en main
- Menú categoría: Falta formato y cls
- FIX Menú Libro->Asociación con categoría; Falta mostrar todos los libros
- FIX Menú categoría->consultar subcategoría (posible replanteamiento de subcategorías)
- Borrar debug generar_copias
- En todos los menús, poner la opcion "0) Salir" al final

- Menú lector->Modificar lector->Estado: Error

- Menú libro->Registrar libro->añadir autores: Se pueden asociar los autores  y no se valida si ya están asociados.

"""
def menu():
    band = True
    while band:
        clear_console()
        opcion = pedir_entero("--- Menú gestor biblioteca ---\n\n1) Menu Artículo Científico\n2) Menu Autor\n3) Menu Categoría\n4) Menu Copia\n5) Menu Lector\n6) Menu Libro\n7) Menu Multa\n8) Menu Prestamo\n9) Menu Tesis\n0) Salir\n\nSeleccione una opción: ", True)
        if opcion == 1:
            menu_articulo()
        elif opcion == 2:
            menu_autor()
        elif opcion == 3:
            menu_categoria()
        elif opcion == 4:
            menu_copia()
        elif opcion == 5:
            menu_lector()
        elif opcion == 6:
            menu_libro()
        elif opcion == 7:
            menu_multa()
        elif opcion == 8:
            menu_prestamo()
        elif opcion == 9:
            menu_tesis()
        elif opcion == 0:
            print("Saliendo del programa...")
            band = False
        else:
            clear_console()
            print("Opción no válida. Intente de nuevo.")
            esperar()

if __name__=="__main__":
    libro = Libro("1",1,1,1,1,1,1,1)
    menu()
    