from gestor_biblioteca.Libro import Libro

#estructuras para almacenar los objetos
libros=[]

if __name__=="__main__":
    libros.append(Libro("978-3-16-148410-0", "El gran libro", 1, 2020, "Editorial XYZ", "Ficción", "Español", 5))
    print(libros[0].get_titulo())