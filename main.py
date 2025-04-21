from gestor_biblioteca.ArticuloCientifico import *
from gestor_biblioteca.Autor import *
from gestor_biblioteca.Categoria import *
from gestor_biblioteca.Copia import *
from gestor_biblioteca.Lector import *
from gestor_biblioteca.Libro import *
from gestor_biblioteca.Multa import *
from gestor_biblioteca.Prestamo import *
from gestor_biblioteca.Tesis import *

if __name__=="__main__":
    Lector("1", "Juan", "3133133", "Calle 123")
    libro = Libro("1", "Libro 1", 1, 1, "Checho", "Terror", "Español", 0)
    Copia.generar_copias(1, libro)
    Tesis(1, "Tesis", "Checho", "12/02/2020", "12/02/2021", "Tesis", 123)
    ArticuloCientifico("1", "Articulo 1", "Checho", "12/02/2020", "Times", "mensual", 12, "Ciencia")

    menu_prestamo()