from share import *
from gestor_biblioteca.Copia import Copia
from gestor_biblioteca.Lector import Lector

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
