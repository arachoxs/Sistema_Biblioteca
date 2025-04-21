from gestor_biblioteca.share import pedir_entero
from gestor_biblioteca.Autor import Autor
from gestor_biblioteca.share import *

class AutorLibro:
    _instancias = []

    def __init__(self, libro, autor):
        self.__autor = autor
        self.__libro = libro

        AutorLibro._instancias.append(self)

    # getters
    def get_autor(self):
        return self.__autor

    def get_libro(self):
        return self.__libro
    
    # setters
    def set_autor(self, autor):
        self.__autor = autor
    
    def set_libro(self, libro):
        self.__libro = libro
        
    def relacionar_autor_libro(libro):
        from gestor_biblioteca.Libro import Libro
        clear_console()
        
        while True:
            print("\n--- Autores disponibles ---")
            print("0. Agregar nuevo autor")
            Autor.mostrar_autores() # Mostrar autores existentes
            opcion = pedir_entero("Seleccione una opción: ") - 1

            # Registrar nuevo autor
            if opcion == -1:
                Autor.registrar() # Agregar nuevo autor
                autor_sel = Autor._instancias[-1] # Seleccionar el último autor agregado

            # Seleccionar autor existente
            elif 0 <= opcion < len(Autor._instancias):
                autor_sel = Autor.get_instancia_index(opcion) # Obtener el autor seleccionado
                
            else:
                print("Opción no válida, intente nuevamente.")
                continue

            # Crear la relación autor–libro
            AutorLibro(libro,autor_sel)
            print(f"Autor «{autor_sel.get_nombre()}» relacionado correctamente con «{libro.get_titulo()}».")
            
            while True:
                print("\n¿Desea relacionar otro autor?")
                print("1. Sí")
                print("2. No")
                continuar = pedir_entero("Seleccione una opción: ")

                if continuar == 1:
                    break  # Vuelve al inicio del bucle principal
                elif continuar == 2:
                    print("Saliendo de la relación de autores...")
                    return
                else:
                    print("Opción no válida, intente nuevamente.")          

    
    def buscar_libros(autor):
        libros = []
        for autor_libro in AutorLibro._instancias:
            if autor_libro.get_autor() == autor:
                libros.append(autor_libro.get_libro())
                
        if len(libros) == 0:
            print("No hay libros registrados para este autor.")
        else:
            print("Libros registrados para este autor:")
            for i in range(len(libros)):
                print(f"{i+1}) - ID: {libros[i].get_id_libro()} - Título: \"{libros[i].get_titulo()}\"")

    def buscar_autores(libro):
        autores = []
        for autor_libro in AutorLibro._instancias:
            if autor_libro.get_libro() == libro:
                autores.append(autor_libro.get_autor())
        
        if len(autores) == 0:
            print("No hay autores registrados para este libro.")
        else:
            print("Autores registrados para este libro:")
            for i in range(len(autores)):
                print(f"{i+1}) - ID: {autores[i].get_id_autor()} - Nombre: \"{autores[i].get_nombre()}\"")
    