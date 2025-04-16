from gestor_biblioteca.Libro import Libro
from gestor_biblioteca.Categoria import Categoria


if __name__=="__main__":
    Categoria(1,"Ciencia Ficcion","Libros de ciencia ficcion")
    Categoria(2,"Terror","Libros de terror")
    
    Libro(123456789,"El juego de Ender",1,1990,"Planeta","Ciencia Ficcion","Español",5)
    
    Libro.instancias[0].asignar_categoria()
        
    
    print(Libro.instancias[0].consultar())   
    
    