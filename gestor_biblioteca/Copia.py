from gestor_biblioteca.Libro import Libro
from gestor_biblioteca.share import *
import random

def menu_copia():
    band=False
    while(not band):
        clear_console()
        
        opcion=pedir_entero("--- Menú Copia ---\n\n1) Registrar Copia\n2) Consultar Copia\n3) Eliminar Copia\n4) Actualizar Estado de Copia\n5) Generar Copias\n0) Salir\n\nSeleccione una opción: ", True)
        clear_console()
        
        if(opcion==1):
            # print("--- Registrar Copia ---\n")
            Copia.registrar()
            
        elif(opcion==2):
            opcion2=pedir_entero("--- Consultar Copia ---\n\n1) Ver lista de copias registradas\n2) Consultar copia por ID\n0) Salir\n\nSeleccione una opción: ", True)
            clear_console()

            if opcion2 == 1:
                print("--- Lista de copias registradas ---\n")
                Copia.mostrar_copias()

            elif opcion2 == 2:
                id=pedir_entero("--- Consultar Copia por ID ---\n\nIngrese el ID de la copia a consultar: ", True)
                copia=Copia.buscar_copia(id)
                if copia == None:
                    clear_console()
                    print(f"No se encontró la copia con ID {id}.")
                    esperar()
                    continue
                clear_console()
                print("Copia seleccionada:\n")
                Copia.consultar(copia)
            
        elif(opcion==3):
            print("--- Eliminar Copia ---\n")
            id=pedir_entero("Ingrese el ID de la copia a eliminar: ")
            copia=Copia.buscar_copia(id)
            if copia == None:
                clear_console()
                print(f"No se encontró la copia con ID {id}.")
                esperar()
                continue
            clear_console()
            Copia.eliminar(copia)

        elif(opcion==4):
            print("--- Actualizar Estado de Copia ---\n")
            id=pedir_entero("Ingrese el ID de la copia a actualizar: ")
            copia=Copia.buscar_copia(id)
            if copia == None:
                clear_console()
                print(f"No se encontró la copia con ID {id}.")
                esperar()
                continue
            clear_console()
            Copia.actualizar_estado(copia)

        elif(opcion==5):
            print("--- Generar Copias ---\n")
            id=input("Ingrese el ISBN del libro al que desea agregar copias: ")
            libro=Libro.buscar_libro(id)
            if libro == None:
                clear_console()
                print(f"No se encontró el libro con ISBN \"{id}\".")
                esperar()
                continue
            n_copias=pedir_entero("Ingrese la cantidad de copias a generar: ", True)
            Copia.generar_copias(n_copias, libro)

        elif(opcion==0):
            band=True
        
        else:
            print("Opción no válida. Por favor intente nuevamente.")
            esperar()

class Copia:
    _instancias = []

    def __init__(self, id_copia, estado = "Disponible"):
        # Atributos de la copia
        self.id_copia = id_copia
        self.estado = estado
        # Atributos asociados al libro
        # Inicialmente no hay libro asociado
        self.libro = None
        # Se agrega la instancia a la lista de copias
        Copia._instancias.append(self)

    def asociar_libro(self, libro):
        # Se verifica que el libro sea una instancia de la clase Libro
        if not isinstance(libro, Libro):
            raise TypeError("El objeto asociado no es un libro.")
        # Se asocia el libro a la copia
        self.libro = libro
        
    # Getters
    def get_id_copia(self):
        return self.id_copia
    def get_estado(self):
        return self.estado
    def get_libro(self):
        return self.libro
    
    # Setters
    def set_id_copia(self, id_copia):
        self.id_copia = id_copia
    def set_estado(self, estado):
        self.estado = estado
    def set_libro(self, libro):
        self.libro = libro

    # Métodos de la clase
    @classmethod
    def buscar_copia(cls, id_copia):
        for copia in cls._instancias:
            if copia.get_id_copia() == id_copia:
                return copia
        return None
    
    @classmethod
    def mostrar_copias(cls):
        if len(cls._instancias) == 0:
            print("No hay copias registradas.")
            esperar()
        else:
            for i in range(len(cls._instancias)):
                print(f" - ID: {cls._instancias[i].get_id_copia()} - Estado: \"{cls._instancias[i].get_estado()}\"")
            esperar()

    def registrar():
        while True:
            clear_console()
            print("--- Registrar Copia ---\n")
            id_copia = pedir_entero("Ingrese el ID de la copia (deje en blanco para una asignación automática): ", False, True)
            if id_copia is None:
                # Generar ID aleatorio de 7 dígitos
                id_copia = random.randint(1000000, 9999999)
                # Verificar si el ID ya existe
                if Copia.buscar_copia(id_copia) is None:
                    break
            else:
                if Copia.buscar_copia(id_copia) is not None:
                    clear_console()
                    print("ID ya registrado. Pruebe con otro valor.")
                    esperar()
                else:
                    break

        libro = Libro.buscar_libro(input("Ingrese el ISBN del libro asociado: "))
        if libro is None:
            clear_console()
            print("No se pudo registrar la copia: Libro no encontrado.")
            esperar()
            return
        estado = "Disponible"

        Copia(id_copia, estado).asociar_libro(libro)
        libro.set_n_copias(libro.get_n_copias() + 1)
        libro.set_activo(True)

        clear_console()
        print(f"Copia con ID {id_copia} registrada correctamente.")
        esperar()

    def consultar(self):
        print(f"ID Copia: {self.id_copia}")
        print(f"Estado: {self.estado}")
        print(f"ISBN de libro asociado: \"{self.libro.get_isbn()}\"")
        esperar()

    def eliminar(self):
        if self.estado != "Disponible":
            clear_console()
            print("No se puede eliminar la copia porque no está disponible en la biblioteca.")
            esperar()
            return
        
        # Se guarda el ID de la copia para mostrarlo después de eliminarla
        id = self.get_id_copia()
        # Se elimina la copia de la lista de instancias
        Copia._instancias.remove(self)
        # Se actualiza el libro asociado
        self.libro.set_n_copias(self.libro.get_n_copias() - 1)
        if self.libro.get_n_copias() == 0:
            self.libro.set_activo(False)
        if self.libro.get_n_copias() < 0:
            self.libro.set_n_copias(0)
        
        # Se eliminan los atributos de la copia
        self.libro = None
        self.estado = None
        self.id_copia = None

        clear_console()
        print(f"Copia con ID {id} eliminada con exito.")
        esperar()

    def actualizar_estado(self):
        clear_console()
        print(f"Copia seleccionada:\n")
        Copia.consultar(self)
        print("\n--- Actualización de Estado ---\n\n1) Disponible\n2) Prestada\n3) Con Retraso\n4) En Reparación\n")
        estado = pedir_entero(f"Seleccione una opción: ")
        if estado == 1:
            estado = "Disponible"
        elif estado == 2:
            estado = "Prestada"
        elif estado == 3:
            estado = "Con Retraso"
        elif estado == 4:
            estado = "En Reparación"
        else:
            clear_console()
            print("Opción no válida. Intente nuevamente.")
            esperar()
            self.actualizar_estado()
            return
        
        # Se actualiza el estado de la copia
        self.estado = estado

        clear_console()
        print(f"Estado de la copia con ID {self.id_copia} actualizado a \"{self.estado}\".")
        esperar()

    @classmethod
    def generar_copias(cls, n_copias, libro):
        ids_existentes = {copia.get_id_copia() for copia in cls._instancias}
        
        for _ in range(n_copias):
            while True:
                # Generar ID aleatorio de 7 dígitos
                id_copia = random.randint(1000000, 9999999)
                # Verificar si el ID ya existe
                if id_copia not in ids_existentes:
                    ids_existentes.add(id_copia) # Añadir el nuevo ID al conjunto para futuras comprobaciones
                    break
            
            # Crear nueva instancia de Copia
            nueva_copia = cls(id_copia) # El estado por defecto es "Disponible"
            # Asociar el libro a la nueva copia
            nueva_copia.asociar_libro(libro)
            print(f"Copia con ID {id_copia} generada y asociada al libro '{libro.get_titulo()}'.")
            esperar()

        clear_console()
        if n_copias == 1:
            print(f"Una copia generada y asociada con éxito al libro '{libro.get_titulo()}'.")
        else:
            print(f"{n_copias} copias generadas y asociadas con éxito al libro '{libro.get_titulo()}'.")

        esperar()
