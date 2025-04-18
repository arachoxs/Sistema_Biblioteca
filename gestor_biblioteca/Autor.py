from gestor_biblioteca.share import *

class Autor:
    _instancias=[]
    
    def __init__(self,id_autor,nombre,nacionalidad,fecha_nacimiento):
        self.__id_autor=id_autor
        self.__nombre=nombre
        self.__nacionalidad=nacionalidad
        self.__fecha_nacimiento=fecha_nacimiento
        Autor._instancias.append(self)
        
    #getters
    def get_id_autor(self):
        return self.__id_autor
    def get_nombre(self):
        return self.__nombre
    def get_nacionalidad(self):
        return self.__nacionalidad
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    #setters
    def set_id_autor(self,id_autor):
        self.__id_autor=id_autor
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_nacionalidad(self,nacionalidad):
        self.__nacionalidad=nacionalidad
    def set_fecha_nacimiento(self,fecha_nacimiento):
        self.__fecha_nacimiento=fecha_nacimiento
        
    #metodos de instancias    
        
    def buscar_autor(id_autor):
        for autor in Autor._instancias:
            if autor.get_id_autor() == id_autor:
                return autor
        return None
    
    def mostrar_autores():
        if len(Autor._instancias) == 0:
            print("No hay autores registrados")
        else:
            for i in range(len(Autor._instancias)):
                print(i+1,". ",Autor._instancias[i].get_nombre())
    
    def get_instancia_index(index):
        return Autor._instancias[index]
    
    def registrar():
        band=False
        while(not band):
            id_autor= pedir_entero("Ingrese el id del autor: ")
            if Autor.buscar_autor(id_autor) == None:
                band=True
            else:
                print("El id ya existe, pruebe con otro valor")

        nombre= input("Ingrese el nombre del autor: ")
        nacionalidad= input("Ingrese la nacionalidad del autor: ")
        print("--- ingrese fecha nacimiento autor ---")
        fecha_nacimiento = Date.registrar_fecha()
       
        Autor(id_autor,nombre,nacionalidad,fecha_nacimiento)         
        print("Autor registrado correctamente")
        
    def consultar(self):
        print("ID Autor: ", self.__id_autor)
        print("Nombre: ", self.__nombre)
        print("Nacionalidad: ", self.__nacionalidad)
        print("Fecha de Nacimiento: ", self.__fecha_nacimiento)
        
        
    def modificar(self):
        band=False
        print("---autor seleccionado---")
        self.consultar()
        
        while(not band):
            print("\n\n---Que desea modificar?---")
            print("1. Nombre")
            print("2. Nacionalidad")
            print("3. Fecha de Nacimiento")
            print("0. Salir")
            
            opcion=pedir_entero("Seleccione una opcion: ")
            
            if(opcion==1):
                nombre = input("Ingrese el nuevo nombre del autor: ")
                self.set_nombre(nombre)
                
            elif(opcion==2):
                nacionalidad = input("Ingrese la nueva nacionalidad del autor: ")
                self.set_nacionalidad(nacionalidad)
                
            elif(opcion==3):
                print("--- ingrese fecha nacimiento autor ---")
                fecha_nacimiento= Date.registrar_fecha()
                self.set_fecha_nacimiento(fecha_nacimiento)
                
            elif(opcion==0):
                band=True
            else:
                print("Opcion no valida, pruebe nuevamente")
        