from gestor_biblioteca.Libro import Libro
from gestor_biblioteca.Categoria import Categoria


if __name__=="__main__":
    Categoria(1,"Ciencia Ficcion","Libros de ciencia ficcion")
    Categoria(2,"Terror","Libros de terror")
    
    Libro.registrar()
    Libro._instancias[0].consultar()

    