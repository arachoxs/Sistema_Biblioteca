from gestor_biblioteca.share import pedir_entero , pedir_nombre
from gestor_biblioteca.Categoria import Categoria
from gestor_biblioteca.Autor import Autor
from gestor_biblioteca.AutorLibro import AutorLibro

def menu_libro():
        band=True
        while(band):
            print("\n\n---Menu libro---")
            print("1. Registrar libro")
            print("2. Consultar libro")
            print("3. Modificar libro")
            print("4. Inhabilitar libro")
            print("0. Salir")
            
            opcion=pedir_entero("Seleccione una opcion: ")
            
            if(opcion==1):
                print("---Registrar libro---")
                Libro.registrar()
                
            elif(opcion==2):
                isbn = input("Ingrese el ISBN del libro a consultar: ")
                libro=Libro.buscar_libro(isbn)
                if(libro!=None):
                    libro.consultar()
                else:
                    print("El libro no existe")
                    
            elif(opcion==3):
                isbn = input("Ingrese el ISBN del libro a modificar: ")
                libro=Libro.buscar_libro(isbn)
                if(libro!=None):
                    libro.modificar()
                else:
                    print("El libro no existe")
                    
            elif(opcion==4):
                isbn = input("Ingrese el ISBN del libro a inhabilitar: ")
                libro=Libro.buscar_libro(isbn)
                if(libro!=None):
                    libro.inhabilitar()
                    print("Libro inhabilitado correctamente")
                else:
                    print("El libro no existe")
                    
            elif(opcion==0):
                band=False
                print("Saliendo del menu de libros...")
                
            else:
                print("Opcion no valida, intente nuevamente")

class Libro:
    _instancias=[]
    
    
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
        
        Libro._instancias.append(self)
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
        
    #metodos de instancias    
    def buscar_libro(isbn):
        for libro in Libro._instancias:
            if libro.get_isbn() == isbn:
                return libro
        return None
    
    def registrar():
        from gestor_biblioteca.Copia import Copia  # Importación dentro del método
        
        isbn = input("Ingrese el ISBN del libro: ")
        
        #veificar unicidad del isbn
        while Libro.buscar_libro(isbn) != None:
            print("El ISBN ya existe, pruebe con otro valor")
            isbn = input("Ingrese el ISBN del libro: ")
        
        titulo = input("Ingrese el titulo del libro: ")
        edicion = pedir_entero("Ingrese la edicion del libro: ")
        año = pedir_entero("Ingrese el año del libro: ")
        editorial = input("Ingrese la editorial del libro: ")
        genero = input("Ingrese el genero del libro: ")
        idioma = input("Ingrese el idioma del libro: ")
        n_copias = pedir_entero("Ingrese el número de copias del libro: ")
        
        #numero copias mayor o igual a 1
        while n_copias < 1:
            print("El número de copias debe ser mayor o igual a 1")
            n_copias = pedir_entero("Ingrese el número de copias del libro: ")
        
        libro = Libro(isbn, titulo, edicion, año, editorial, genero, idioma, n_copias) #crea libro
        libro.asignar_categoria() # Asignar categoría al libro
        AutorLibro.relacionar_autor_libro(libro) # Relacionar autor al libro
        # Crear copias del libro
        Copia.generar_copias(n_copias, libro)  # Corrige el orden de los parámetros
        
        print("Libro registrado correctamente")
        
        
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
            print("Categoria: ", self.__categoria_libro.get_nombre())
        print("--Autores libro--")
        AutorLibro.buscar_autores(self)
                
    def modificar(self):
        if(self.__activo!=True):
            print("El libro no se encuentra activo, no se puede modificar")
            return
        
        print("---Libro seleccionado---")
        self.consultar()
        band=True
        while(band):
            print("\n\n---Que desea modificar?---")
            print("1. Titulo")
            print("2. Edicion")
            print("3. Año")
            print("4. Editorial")
            print("5. Genero")
            print("6. Idioma")
            print("7. Asignar nueva Categoria")
            print("8. Asignar nuevo autor")
            print("9. Desactivar libro")
            print("0. Salir")
            
            opcion=pedir_entero("Seleccione una opcion: ")
               
            if(opcion==1):
                titulo = input("Ingrese el nuevo titulo del libro: ")
                self.set_titulo(titulo)
                
            elif(opcion==2):
                edicion = pedir_entero("Ingrese la nueva edicion del libro: ")
                self.set_edicion(edicion)
                
            elif(opcion==3):
                año = pedir_entero("Ingrese el nuevo año del libro: ")
                self.set_año(año)
                
            elif(opcion==4):
                editorial = input("Ingrese la nueva editorial del libro: ")
                self.set_editorial(editorial)
                
            elif(opcion==5):
                genero = input("Ingrese el nuevo genero del libro: ")
                self.set_genero(genero)
                
            elif(opcion==6):
                idioma = input("Ingrese el nuevo idioma del libro: ")
                self.set_idioma(idioma)
                
            elif(opcion==7):
                self.asignar_categoria()
                
            elif(opcion==8):
                AutorLibro.relacionar_autor_libro(self)
                print("Autor relacionado correctamente.")
                
            elif(opcion==9):
                self.inhabilitar()
                print("Libro desactivado correctamente")
                
            elif(opcion==0):
                band=False
                print("Saliendo de la modificacion del libro...")
            else:   
                print("Opcion no valida, intente nuevamente")
                
        
    def inhabilitar(self):
        self.__activo=False
        
    def asignar_categoria(self):
        band=True
        if self.__activo!=True:
            print("El libro no se encuentra activo, no se puede asignar categoria")
            return
        if len(Categoria._instancias)==0:
            print("No hay categorias disponibles para asignar")
            return
        while(band):
            print("Categorias disponibles:")
            Categoria.mostrar_instancias()
            print("0. Salir")
            
            opcion=pedir_entero("Seleccione una categoria: ")
            opcion-=1
            
            if(opcion>=0 and opcion<len(Categoria._instancias)):
                self.__categoria_libro=Categoria.get_instancia_index(opcion)
                print("Categoria asignada correctamente")
                band=False
            else:
                print("Opcion no valida, intente nuevamente")
                
    