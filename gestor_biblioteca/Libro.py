from gestor_biblioteca.share import pedir_entero

class Libro:
    def __init__(self, isbn , titulo , edicion , año , editorial, genero , idioma , n_copias, activo=True):
        self.__isbn=isbn
        self.__titulo=titulo
        self.__edicion=edicion
        self.__año=año
        self.__editorial=editorial
        self.__genero=genero
        self.__idioma=idioma
        self.__n_copias=n_copias
        self.__activo=activo
        self.__categoria_libro=None

    #getters
    def get_isbn(self):
        return self.__isbn
    def get_titulo(self):
        return self.__titulo
    def get_edicion(self):
        return self.__edicion
    def get_año(self):
        return self.__año
    def get_editorial(self):
        return self.__editorial
    def get_genero(self):
        return self.__genero
    def get_idioma(self):
        return self.__idioma
    def get_n_copias(self):
        return self.__n_copias
    def get_activo(self):
        return self.__activo
    
    #setters
    def set_isbn(self, isbn):
        self.__isbn=isbn
    def set_titulo(self, titulo):
        self.__titulo=titulo
    def set_edicion(self, edicion):
        self.__edicion=edicion
    def set_año(self, año):
        self.__año=año
    def set_editorial(self, editorial):
        self.__editorial=editorial
    def set_genero(self, genero):
        self.__genero=genero
    def set_idioma(self, idioma):
        self.__idioma=idioma
    def set_n_copias(self, n_copias):
        self.__n_copias=n_copias
    def set_activo(self, activo):
        self.__activo=activo
    
    def registrar():
        isbn = input("Ingrese el ISBN del libro: ")
        titulo = input("Ingrese el titulo del libro: ")
        edicion = pedir_entero("Ingrese la edicion del libro: ")
        año = pedir_entero("Ingrese el año del libro: ")
        editorial = input("Ingrese la editorial del libro: ")
        genero = input("Ingrese el genero del libro: ")
        idioma = input("Ingrese el idioma del libro: ")
        n_copias = pedir_entero("Ingrese el número de copias del libro: ")
        
        return Libro(isbn,titulo,edicion,año,editorial,genero,idioma,n_copias)
        
    def consultar(self):
        print("ISBN: ", self.__isbn)
        print("Titulo: ", self.__titulo)
        print("Edicion: ", self.__edicion)
        print("Año: ", self.__año)
        print("Editorial: ", self.__editorial)
        print("Genero: ", self.__genero)
        print("Idioma: ", self.__idioma)
        print("Numero de copias: ", self.__n_copias)
        if(self.__activo==True):
            print("Estado: Activo")
        else:
            print("Estado: Inactivo")
        if(self.__categoria_libro==None):
            print("Categoria: No asignada")
        else:
            print("Categoria: ", self.__categoria_libro.get_nombre_categoria())
    
    def inhabilitar(self):
        self.__activo=False
        