from share import pedir_entero
from gestor_biblioteca.Autor import Autor
from gestor_biblioteca.Libro import Libro

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
    
    def buscar_libros(self, autor):
        libros = []
        for autor_libro in AutorLibro._instancias:
            if autor_libro.get_autor() == autor:
                libros.append(autor_libro.get_libro())
        return libros

    def buscar_autores(self, libro):
        autores = []
        for autor_libro in AutorLibro._instancias:
            if autor_libro.get_libro() == libro:
                autores.append(autor_libro.get_autor())
        return autores
    