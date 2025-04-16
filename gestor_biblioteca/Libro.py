from gestor_biblioteca.share import pedir_entero
from gestor_biblioteca.Categoria import Categoria

class Libro:
    instancias=[]
    
    
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
        
        Libro.instancias.append(self)

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
        
        Libro(isbn,titulo,edicion,año,editorial,genero,idioma,n_copias)
        
        
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
            
    def modificar(self):
        print("---Libro seleccionado---")
        self.consultar()
        band=True
        while(band):
            print("\n\nQue desea modificar?")
            print("1. ISBN")
            print("2. Titulo")
            print("3. Edicion")
            print("4. Año")
            print("5. Editorial")
            print("6. Genero")
            print("7. Idioma")
            print("8. Numero de copias")
            print("9. Categoria")
            print("0. Salir")
            
            opcion=pedir_entero("Seleccione una opcion: ")
            
            if(opcion==1):
                isbn = input("Ingrese el nuevo ISBN del libro: ")
                self.set_isbn(isbn)
                
            elif(opcion==2):
                titulo = input("Ingrese el nuevo titulo del libro: ")
                self.set_titulo(titulo)
                
            elif(opcion==3):
                edicion = pedir_entero("Ingrese la nueva edicion del libro: ")
                self.set_edicion(edicion)
                
            elif(opcion==4):
                año = pedir_entero("Ingrese el nuevo año del libro: ")
                self.set_año(año)
                
            elif(opcion==5):
                editorial = input("Ingrese la nueva editorial del libro: ")
                self.set_editorial(editorial)
                
            elif(opcion==6):
                genero = input("Ingrese el nuevo genero del libro: ")
                self.set_genero(genero)
                
            elif(opcion==7):
                idioma = input("Ingrese el nuevo idioma del libro: ")
                self.set_idioma(idioma)
                
            elif(opcion==8):
                n_copias = pedir_entero("Ingrese el nuevo numero de copias del libro: ")
                self.set_n_copias(n_copias)

            elif(opcion==9):
                categoria_libro=input("Ingrese la nueva categoria del libro: ") #cambiar por la funcion asignar categoria
                
            elif(opcion==0):
                band=False
                print("Saliendo de la modificacion del libro...")
            else:   
                print("Opcion no valida, intente nuevamente")
                
        
    def inhabilitar(self):
        self.__activo=False
        
    def asignar_categoria(self):
        band=True
        while(band):
            print("Categorias disponibles:")
            for(index in range (0, len(Categoria.instancias))):
                print(index, Categoria.instancias[index].get_nombre_categoria())
            
            opcion=pedir_entero("Seleccione una categoria: ")
            if(opcion>=0 and opcion<len(Categoria.instancias)):
                self.__categoria_libro=Categoria.instancias[opcion]
                print("Categoria asignada correctamente")
                band=False
            else:
                print("Opcion no valida, intente nuevamente")