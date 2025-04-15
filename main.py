from gestor_biblioteca.Libro import Libro



if __name__=="__main__":
    Libro("978-3-16-148410-0", "El gran libro", 1, 2020, "Editorial XYZ", "Ficción", "Español", 5)
    
    print(Libro.instancias[0].get_titulo())
   
    