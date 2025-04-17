from gestor_biblioteca.share import pedir_entero

class Categoria:
    instancias=[]
    
    def __init__(self,idCategoria,nombre,descripcion):
        self.__idCategoria=idCategoria
        self.__nombre=nombre
        self.__descripcion=descripcion
        Categoria.instancias.append(self)

    #getters
    def get_idCategoria(self):
        return self.__idCategoria
    def get_nombre(self):
        return self.__nombre
    def get_descripcion(self):
        return self.__descripcion
    
    #setters
    def set_idCategoria(self,idCategoria):
        self.__idCategoria=idCategoria
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_descripcion(self,descripcion):
        self.__descripcion=descripcion

    #metodos
    def crear():
        idCategoria=pedir_entero(input("Ingrese el id de la categoria: "))
        nombre=input("Ingrese el nombre de la categoria: ")
        descripcion=input("Ingrese la descripcion de la categoria: ")
    
        Categoria(idCategoria,nombre,descripcion)

    def consultar(self):
        print("ID Categoria: ", self.__idCategoria)
        print("Nombre: ", self.__nombre)
        print("Descripcion: ", self.__descripcion)

    def modificar(self):
        print("ID Categoria: ", self.__idCategoria)
        print("Nombre: ", self.__nombre)
        print("Descripcion: ", self.__descripcion)
        
        idCategoria=pedir_entero(input("Ingrese el nuevo id de la categoria: "))
        nombre=input("Ingrese el nuevo nombre de la categoria: ")
        descripcion=input("Ingrese la nueva descripcion de la categoria: ")
        
        self.set_idCategoria(idCategoria)
        self.set_nombre(nombre)
        self.set_descripcion(descripcion)

    def eliminar(self):
        print("ID Categoria: ", self.__idCategoria)
        print("Nombre: ", self.__nombre)
        print("Descripcion: ", self.__descripcion)
        
        respuesta = input("¿Está seguro que desea eliminar la categoría? (s/n): ")
        
        if respuesta.lower() == "s":
            Categoria.instancias.remove(self)
            print("Categoría eliminada")
        else:
            print("Categoría no eliminada")
