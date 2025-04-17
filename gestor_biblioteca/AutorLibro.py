from gestor_biblioteca.share import pedir_entero
from gestor_biblioteca.Autor import Autor

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
        
        while True:
            print("\n--- Autores disponibles ---")
            print("0. Agregar nuevo autor")
            for idx, autor_inst in enumerate(Autor._instancias, start=1):
                print(f"{idx}. {autor_inst.get_nombre()}")

            opcion = pedir_entero("Seleccione una opción: ") - 1

            # Registrar nuevo autor
            if opcion == -1:
                Autor.registrar()
                autor_sel = Autor._instancias[-1]

            # Seleccionar autor existente
            elif 0 <= opcion < len(Autor._instancias):
                autor_sel = Autor._instancias[opcion]

            else:
                print("Opción no válida, intente nuevamente.")
                continue

            # Crear la relación autor–libro
            AutorLibro(libro,autor_sel)
            print(f"Autor «{autor_sel.get_nombre()}» relacionado correctamente con «{libro.get_titulo()}».")
            break
    
    def buscar_libros(autor):
        libros = []
        for autor_libro in AutorLibro._instancias:
            if autor_libro.get_autor() == autor:
                print(autor_libro.get_libro().get_titulo())
                
        return libros

    def buscar_autores(libro):
        autores = []
        for autor_libro in AutorLibro._instancias:
            if autor_libro.get_libro() == libro:
                autores.append(autor_libro.get_autor())
        return autores
    