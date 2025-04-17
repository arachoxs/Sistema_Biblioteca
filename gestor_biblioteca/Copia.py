from gestor_biblioteca.Libro import Libro
import random

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
    
    def registrar(self):
        while True: 
            id_copia = input("Ingrese el ID de la copia (deje en blanco para una asignación automática): ")
            ids_existentes = {copia.get_id_copia() for copia in Copia._instancias}
            if id_copia == "":
                # Generar ID aleatorio de 7 dígitos
                id_copia = random.randint(1000000, 9999999)
                # Verificar si el ID ya existe
                if id_copia not in ids_existentes:
                        break
            else:
                if id_copia in ids_existentes:
                    print("ID ya registrado. Pruebe con otro valor.")
                else:
                    break

        libro = Libro.buscar_libro(input("Ingrese el ISBN del libro asociado: "))
        if libro is None:
            print("No se pudo registrar la copia: Libro no encontrado.")
            return
        estado = "Disponible"

        Copia(id_copia, estado).asociar_libro(libro)
        libro.set_n_copias(libro.get_n_copias() + 1)
        libro.set_activo(True)

        print(f"Copia con ID {id_copia} registrada con exito.")

    def consultar(self):
        print(f"ID: {self.id_copia}")
        print(f"Estado: {self.estado}")
        print(f"ISBN de libro asociado: {self.libro.get_isbn()}")

    def eliminar(self):
        if self.estado != "Disponible":
            print("No se puede eliminar la copia porque no está disponible en la biblioteca.")
            return
        
        Copia._instancias.remove(self)
        self.libro.set_n_copias(self.libro.get_n_copias() - 1)
        if self.libro.get_n_copias() == 0:
            self.libro.set_activo(False)
        if self.libro.get_n_copias() < 0:
            self.libro.set_n_copias(0)
        self.libro = None
        self.estado = None
        self.id_copia = None

        print(f"Copia con ID {self.id_copia} eliminada con exito.")

    def actualizar_estado(self):
        print("Seleccione una opción:\n1. Disponible\n2. Prestada\n3. Con Retraso\n4. En Reparación")
        opcion = input("Opción: ")
        if opcion == "1":
            self.estado = "Disponible"
        elif opcion == "2":
            self.estado = "Prestada"
        elif opcion == "3":
            self.estado = "Con Retraso"
        elif opcion == "4":
            self.estado = "En Reparación"
        else:
            print("Opción no válida.")
            return
        print(f"Estado de la copia con ID {self.id_copia} actualizado a {self.estado}.")

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
            # print(f"Copia con ID {id_copia} generada y asociada al libro '{libro.get_titulo()}'.")
        if n_copias == 1:
            print(f"Una copia generada y asociada con éxito al libro '{libro.get_titulo()}'.")
        else:
            print(f"{n_copias} copias generadas y asociadas con éxito al libro '{libro.get_titulo()}'.")

            
