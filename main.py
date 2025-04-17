from gestor_biblioteca.Libro import Libro
from gestor_biblioteca.Categoria import Categoria
from gestor_biblioteca.Autor import Autor
from gestor_biblioteca.AutorLibro import AutorLibro


if __name__=="__main__":
    autor1=Autor(1, "Autor Ejemplo", "Español", "01/01/1980")
    libro1=Libro(123456789, "Libro Ejemplo", "Primera Edición", 2023, "Editorial Ejemplo", "Ficción", "Español", 5)
    AutorLibro.relacionar_autor_libro(libro1)
    libro1.consultar()
    print("---camvbio...")
    AutorLibro.buscar_libros(autor1)