from gestor_biblioteca.Libro import Libro
from gestor_biblioteca.Categoria import Categoria
from gestor_biblioteca.Autor import Autor


if __name__=="__main__":
    libro1=Libro("978-3-16-148410-0", "Ejemplo de Libro", 1, 2023, "Editorial Ejemplo", "Ficción", "Español", 5)
    autor1=Autor(1, "Autor Ejemplo", "Español", "01/01/1980")
    libro1.consultar()
    libro1.relacionar_autor()

    