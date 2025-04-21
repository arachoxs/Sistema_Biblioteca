from gestor_biblioteca.share import *

def menu_lector():
    band=False
    while(not band):
        clear_console()
        
        opcion=pedir_entero("--- Menú Lector ---\n\n1) Registrar Lector\n2) Consultar Lector\n3) Modificar Lector\n4) Inhabilitar Lector\n5) Habilitar Lector\n0) Salir\n\nSeleccione una opción: ", True)
        clear_console()
        
        if(opcion==1):
            # print("--- Registrar Lector ---\n")
            Lector.registrar()
            
        elif(opcion==2):
            opcion2=pedir_entero("--- Consultar Lector ---\n\n1) Ver lista de lectores\n2) Consultar lector por ID\n0) Salir\n\nSeleccione una opción: ", True)
            clear_console()

            if opcion2 == 1:
                print("--- Lista de lectores registrados ---\n")
                Lector.mostrar_lectores()

            elif opcion2 == 2:
                id=input("--- Consultar Lector por ID ---\n\nIngrese el ID del lector a consultar: ")
                lector=Lector.buscar_lector(id)
                if lector == None:
                    clear_console()
                    print(f"No se encontró el lector con ID \"{id}\".")
                    esperar()
                    continue
                clear_console()
                print("Lector seleccionado:\n")
                Lector.consultar(lector)
            
        elif(opcion==3):
            print("--- Modificar Lector ---\n")
            id=input("Ingrese el ID del lector a modificar: ")
            lector=Lector.buscar_lector(id)
            if lector == None:
                clear_console()
                print(f"No se encontró el lector con ID \"{id}\".")
                esperar()
                continue
            clear_console()
            Lector.modificar(lector)
                
        elif(opcion==4):
            print("--- Inhabilitar Lector ---\n")
            id=input("Ingrese el ID del lector a inhabilitar: ")
            lector=Lector.buscar_lector(id)
            if lector == None:
                clear_console()
                print(f"No se encontró el lector con ID \"{id}\".")
                esperar()
                continue
            clear_console()
            Lector.inhabilitar(lector)

        elif(opcion==5):
            print("--- Habilitar Lector ---\n")
            id=input("Ingrese el ID del lector a habilitar: ")
            lector=Lector.buscar_lector(id)
            if lector == None:
                clear_console()
                print(f"No se encontró el lector con ID \"{id}\".")
                esperar()
                continue
            clear_console()
            Lector.habilitar(lector)
        
        elif(opcion==0):
            band=True

        else:
            clear_console()
            print("Opción no válida. Por favor intente nuevamente.")
            esperar()
        

class Lector:
    _instancias = []

    def __init__(self, id_lector, nombre, telefono, direccion, estado = "Normal"):
        # Atributos del lector
        self.id_lector = id_lector
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.estado = estado
        self.estado_previo = estado
        # Se agrega la instancia a la lista de lectores
        Lector._instancias.append(self)

    # Getters
    def get_id_lector(self):
        return self.id_lector
    def get_nombre(self):
        return self.nombre
    def get_telefono(self):
        return self.telefono
    def get_direccion(self):
        return self.direccion
    def get_estado(self):
        return self.estado
    
    # Setters
    def set_id_lector(self, id_lector):
        self.id_lector = id_lector
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_telefono(self, telefono):
        self.telefono = telefono
    def set_direccion(self, direccion):
        self.direccion = direccion
    def set_estado(self, estado):
        self.estado = estado

    # Métodos de la clase
    @classmethod
    def buscar_lector(cls, id_lector):
        for lector in cls._instancias:
            if lector.get_id_lector() == id_lector:
                return lector
        return None
    
    @classmethod
    def mostrar_lectores(cls):
        if len(cls._instancias) == 0:
            print("No hay lectores registrados.")
            esperar()
        else:
            for i in range(len(cls._instancias)):
                print(f" - ID: \"{cls._instancias[i].get_id_lector()}\" - Nombre: \"{cls._instancias[i].get_nombre()}\"")
            esperar()

    def registrar():
        while True:
            clear_console()
            print("--- Registrar Lector ---\n")
            id_lector = input("Ingrese el ID del lector: ")
            if Lector.buscar_lector(id_lector) is None:
                break
            print("ID ya registrado. Pruebe con otro valor.")
            esperar()
        nombre = input("Ingrese el nombre del lector: ")
        telefono = input("Ingrese el teléfono del lector: ")
        direccion = input("Ingrese la dirección del lector: ")
        estado = "Normal"

        Lector(id_lector, nombre, telefono, direccion, estado)
        print(f"\nLector con ID {id_lector} registrado correctamente.")
        esperar()

    def consultar(self):
        print(f"ID Lector: {self.id_lector}")
        print(f"Nombre: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")
        print(f"Estado: {self.estado}")
        esperar()

    def modificar(self):
        if self.estado == "Inactivo":
            print("No se puede modificar un lector inactivo.")
            esperar()
            return
        
        band = False
        while(not band):
            clear_console()
            print("--- Lector seleccionado ---\n") 
            self.consultar()
            print("\n--- ¿Qué desea modificar? ---\n")
            print("1) Nombre")
            print("2) Teléfono")
            print("3) Dirección")
            print("4) Estado")
            print("0) Salir\n")

            opcion = pedir_entero("Seleccione una opción: ")

            if opcion == 1:
                nombre = input("Ingrese el nuevo nombre del lector: ")
                self.set_nombre(nombre)

            elif opcion == 2:
                telefono = input("Ingrese el nuevo teléfono del lector: ")
                self.set_telefono(telefono)
            
            elif opcion == 3:
                direccion = input("Ingrese la nueva dirección del lector: ")
                self.set_direccion(direccion)

            elif opcion == 4:
                print("\n--- Selección de Estado ---\n1) Normal\n2) Sancionado\n3) Suspendido\n")
                estado = pedir_entero(f"Seleccione una opción: ")
                if estado == "1":
                    estado = "Normal"
                elif estado == "2":
                    estado = "Sancionado"
                elif estado == "3":
                    estado = "Suspendido"
                else:
                    print("\nOpción no válida. Intente nuevamente.")
                    esperar()
                    continue
                self.set_estado(estado)

            elif opcion == 0:
                band = True

            else:
                print("Opción no válida. Intente nuevamente.")

        clear_console()
        print("Lector modificado correctamente.")
        esperar()

    def inhabilitar(self):
        self.estado_previo = self.estado
        self.set_estado("Inactivo")
        print(f"Lector con ID {self.id_lector} inhabilitado correctamente.")
        esperar()

    def habilitar(self):
        self.estado = self.estado_previo
        print(f"Lector con ID {self.id_lector} habilitado correctamente.")
        esperar()

    def sancionar(self):
        self.set_estado("Sancionado")
        print(f"Lector con ID {self.id_lector} sancionado correctamente.")
        esperar()
    
    def suspender(self):
        self.set_estado("Suspendido")
        print(f"Lector con ID {self.id_lector} suspendido correctamente.")
        esperar()

    
    