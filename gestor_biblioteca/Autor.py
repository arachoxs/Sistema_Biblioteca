from gestor_biblioteca.share import *

def menu_autor():
    band=False
    while(not band):
        clear_console()
        print("--- Menú Autor ---\n")
        print("1. Registrar Autor")
        print("2. Consultar Autor")
        print("3. Modificar Autor")
        print("0. Salir\n")
        
        opcion=pedir_entero("Seleccione una opción: ")
        clear_console()
        
        if(opcion==1):
            print("--- Registrar Autor ---\n")
            Autor.registrar()
            
        elif(opcion==2):
            print("--- Consultar Autor ---\n")
            print("1) Ver lista de autores")
            print("2) Consultar autor por ID")
            print("0) Salir\n")

            opcion2=pedir_entero("Seleccione una opción: ")
            if opcion2 == 1:
                clear_console()
                print("--- Lista de autores registrados ---\n")
                Autor.mostrar_autores()
            elif opcion2 == 2:
                clear_console()
                print("--- Consultar Autor por ID ---\n")
                id=pedir_entero("Ingrese el ID del autor a consultar: ")
                autor=Autor.buscar_autor(id)
                if autor == None:
                    print("No se encontró el autor.")
                    esperar()
                    continue
                clear_console()
                print("Autor seleccionado:\n")
                Autor.consultar(autor)
            
        elif(opcion==3):
            print("--- Modificar Autor ---\n")
            id=pedir_entero("Ingrese el ID del autor a modificar: ")
            autor=Autor.buscar_autor(id)
            if autor == None:
                print("No se encontró el autor.")
                esperar()
                continue
            clear_console()
            Autor.modificar(autor)
                
        elif(opcion==0):
            band=True
            print("Saliendo del menú de autores.")
            esperar()
            
        else:
            print("Opción no válida, intente nuevamente.")
            esperar()
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
            print("No hay autores registrados.")
            esperar()
        else:
            for i in range(len(Autor._instancias)):
                print(f" - ID: {Autor._instancias[i].get_id_autor()} - Nombre: {Autor._instancias[i].get_nombre()}")
            esperar()
    
    def get_instancia_index(index):
        return Autor._instancias[index]
    
    def registrar():
        band=False
        while(not band):
            id_autor= pedir_entero("Ingrese el ID del autor: ")
            if Autor.buscar_autor(id_autor) == None:
                band=True
            else:
                print("El ID ya existe, intente con otro valor.\n")

        nombre= input("Ingrese el nombre del autor: ")
        nacionalidad= input("Ingrese la nacionalidad del autor: ")
        print("Ingrese la fecha nacimiento del autor:\n")
        fecha_nacimiento = Date.registrar_fecha()
       
        Autor(id_autor,nombre,nacionalidad,fecha_nacimiento)         
        print("Autor registrado correctamente.")
        esperar()
        
    def consultar(self):
        print("ID Autor: ", self.__id_autor)
        print("Nombre: ", self.__nombre)
        print("Nacionalidad: ", self.__nacionalidad)
        print("Fecha de Nacimiento: ", self.__fecha_nacimiento)
        esperar()
        
    def modificar(self):
        band=False
        while(not band):
            clear_console()
            print("--- Autor seleccionado ---\n")
            self.consultar()
            print("\n--- ¿Qué desea modificar? ---\n")
            print("1. Nombre")
            print("2. Nacionalidad")
            print("3. Fecha de Nacimiento")
            print("0. Salir\n")
            
            opcion=pedir_entero("Seleccione una opcion: ")
            
            if(opcion==1):
                nombre = input("Ingrese el nuevo nombre del autor: ")
                self.set_nombre(nombre)
                
            elif(opcion==2):
                nacionalidad = input("Ingrese la nueva nacionalidad del autor: ")
                self.set_nacionalidad(nacionalidad)
                
            elif(opcion==3):
                print("Ingrese la nueva fecha nacimiento del autor:\n")
                fecha_nacimiento= Date.registrar_fecha()
                self.set_fecha_nacimiento(fecha_nacimiento)
                
            elif(opcion==0):
                band=True
            else:
                print("Opción no válida, intente nuevamente.")
        