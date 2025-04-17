from share import *
from gestor_biblioteca.Copia import Copia
from gestor_biblioteca.Lector import Lector
import random

class Prestamo:
    _instancias = []

    def __init__(self, id_prestamo, tipo_producto, dias_prestamo, fecha_prestamo, fecha_entrega_estimada, activo = True):
        # Atributos del préstamo
        self.id_prestamo = id_prestamo
        self.tipo_producto = tipo_producto
        self.dias_prestamo = dias_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega_estimada = fecha_entrega_estimada
        self.activo = activo
        # Atributos asociados a la copia y al lector
        # Inicialmente no hay copia ni lector asociados
        self.lector = None
        # Se agrega la instancia a la lista de préstamos
        Prestamo._instancias.append(self)

    def asociar_lector(self, lector):
        # Se verifica que el lector sea una instancia de la clase Lector
        if not isinstance(lector, Lector):
            raise TypeError("El objeto asociado no es un lector.")
        # Se asocia el lector al préstamo
        self.lector = lector

    def asociar_copia(self, copia):
        # Se verifica que la copia sea una instancia de la clase Copia
        if not isinstance(copia, Copia):
            raise TypeError("El objeto asociado no es una copia.")
        # Se asocia la copia al préstamo
        self.copia = copia

    # Getters
    def get_id_prestamo(self):
        return self.id_prestamo
    def get_tipo_producto(self):
        return self.tipo_producto
    def get_dias_prestamo(self):
        return self.dias_prestamo
    def get_fecha_prestamo(self):
        return self.fecha_prestamo
    def get_fecha_entrega_estimada(self):
        return self.fecha_entrega_estimada
    def get_activo(self):
        return self.activo
    def get_copia(self):
        return self.copia
    def get_lector(self):
        return self.lector
    
    # Setters
    def set_id_prestamo(self, id_prestamo):
        self.id_prestamo = id_prestamo
    def set_tipo_producto(self, tipo_producto):
        self.tipo_producto = tipo_producto
    def set_dias_prestamo(self, dias_prestamo):
        self.dias_prestamo = dias_prestamo
    def set_fecha_prestamo(self, fecha_prestamo):
        self.fecha_prestamo = fecha_prestamo
    def set_fecha_entrega_estimada(self, fecha_entrega_estimada):
        self.fecha_entrega_estimada = fecha_entrega_estimada
    def set_activo(self, activo):
        self.activo = activo
    def set_copia(self, copia):
        self.copia = copia
    def set_lector(self, lector):
        self.lector = lector

    # Métodos de la clase
    @classmethod
    def buscar_prestamo(cls, id_prestamo):
        for prestamo in cls._instancias:
            if prestamo.get_id_prestamo() == id_prestamo:
                return prestamo
        return None
    
    def registrar(self):
        # Se busca el lector asociado al préstamo
        lector = Lector.buscar_lector(input("Ingrese el ID del lector asociado: "))
        # Se verifica que el lector sea una instancia de la clase Lector
        if lector is None:
            print("No se pudo registrar el préstamo: Lector no encontrado.")
            return
        # Verificar que el lector no tenga más del máximo de préstamos activos permitido
        prestamos_activos_lector = 0
        # Se define el máximo de préstamos por lector
        # (Este valor puede ser ajustado según las políticas de la biblioteca)
        MAX_PRESTAMOS_POR_LECTOR = 3
        for prestamo_existente in Prestamo._instancias:
            # Verificar si el préstamo está activo y pertenece al lector
            if prestamo_existente.get_lector() == lector and prestamo_existente.get_activo():
                prestamos_activos_lector += 1
        
        if prestamos_activos_lector >= MAX_PRESTAMOS_POR_LECTOR:
            print(f"No se pudo registrar el préstamo: El lector {lector.get_id_lector()} ya tiene {MAX_PRESTAMOS_POR_LECTOR} préstamos activos.")
            return
        
        # Se verifica que el lector esté en estado normal
        if lector.get_estado() != "Normal":
            print("No se pudo registrar el préstamo: El lector no está en estado normal.")
            return

        # Se busca la copia asociada al préstamo        
        copia = Copia.buscar_copia(input("Ingrese el ID de la copia asociada: "))
        # Se verifica que la copia sea una instancia de la clase Copia
        if copia is not None:
            # Se verifica que la copia esté disponible
            if copia.get_estado() != "Disponible":
                print("No se pudo registrar el préstamo: La copia no está disponible.")
                return
        else:
            print("No se pudo registrar el préstamo: Copia no encontrada.")
            return
        
        # Se solicita al usuario la información del préstamo
        while True:
            id_prestamo = input("Ingrese el ID del prestamo (deje en blanco para una asignación automática): ")
            ids_existentes = {prestamo.get_id_prestamo() for prestamo in Prestamo._instancias} # Conjunto de IDs existentes para evitar duplicados
            if id_prestamo == "":
                while True:
                    # Generar ID aleatorio de 7 dígitos
                    id_prestamo = random.randint(1000000, 9999999)
                    # Verificar si el ID ya existe
                    if id_prestamo not in ids_existentes:
                        break
            else:
                if id_prestamo in ids_existentes:
                    print("ID ya registrado. Pruebe con otro valor.")
                else:
                    break
        
        # Se solicita el tipo de producto
        opcion = input("Seleccione el tipo de producto:\n1. Copia de libro\n2. Artículo Científico\n3. Tesis")
        while True:
            if opcion in ["1", "2", "3"]:
                break
            else:
                print("Opción no válida. Intente nuevamente.")
                opcion = input("Seleccione el tipo de producto:\n1. Copia de libro\n2. Artículo Científico\n3. Tesis")
        if opcion == "1":
            tipo_producto = "Copia de libro"
        elif opcion == "2":
            tipo_producto = "Artículo Científico"
        elif opcion == "3":
            tipo_producto = "Tesis"

        dias_prestamo = pedir_entero("Ingrese la cantidad de días de préstamo: ")
        print("Ingrese la fecha de préstamo (DD/MM/AAAA): ")
        fecha_prestamo = Date.registrar_fecha()
        fecha_entrega_estimada = fecha_prestamo.sumar_dias(dias_prestamo)
        activo = True

        # Se crea el préstamo y se asocian la copia y el lector
        prestamo = Prestamo(id_prestamo, tipo_producto, dias_prestamo, fecha_prestamo, fecha_entrega_estimada, activo)
        prestamo.asociar_copia(copia)
        prestamo.asociar_lector(lector)
        # Se cambia el estado de la copia a "Prestada"
        self.copia.set_estado("Prestada")

        print(f"Préstamo con ID {id_prestamo} registrado con éxito.")

    def calcular_fecha_entrega(self):
        """Calcula la fecha de entrega real del préstamo."""
        return self.fecha_prestamo.sumar_dias(self.dias_prestamo)
    
    def consultar(self):
        print(f"ID: {self.id_prestamo}")
        print(f"Tipo de producto: {self.tipo_producto}")
        print(f"Días de préstamo: {self.dias_prestamo}")
        print(f"Fecha de préstamo: {self.fecha_prestamo.get_dia()}/{self.fecha_prestamo.get_mes()}/{self.fecha_prestamo.get_año()}")
        print(f"Fecha de entrega estimada: {self.fecha_entrega_estimada.get_dia()}/{self.fecha_entrega_estimada.get_mes()}/{self.fecha_entrega_estimada.get_año()}")
        print(f"Estado activo: {self.activo}")
        if self.copia is not None:
            print(f"ID de copia asociada: {self.copia.get_id_copia()}")
        if self.lector is not None:
            print(f"ID de lector asociado: {self.lector.get_id_lector()}")
        print(f"Estado del lector: {self.lector.get_estado() if self.lector else 'No asociado'}")
        print(f"Estado de la copia: {self.copia.get_estado() if self.copia else 'No asociado'}")

    def cancelar(self):
        """Cancela el préstamo y actualiza el estado de la copia y el lector."""
        if self.copia is not None:
            self.copia.set_estado("Disponible")
            self.copia = None
        if self.lector is not None:
            self.lector.set_estado("Normal")
            self.lector = None
        self.activo = False
        Prestamo._instancias.remove(self)
        print(f"Préstamo con ID {self.id_prestamo} cancelado con éxito.")