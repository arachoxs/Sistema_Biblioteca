from share import *
from gestor_biblioteca.Prestamo import Prestamo
from gestor_biblioteca.Lector import Lector
class Multa:
    _instancias=[]
    MULTA_DIAS=3
    
    
    def __init__(self,id_multa,lector,fecha_entrega_real,dias_multa,fecha_inicio_multa,fecha_final_multa,activa=True):
        self.__id_multa=id_multa
        self.__lector=lector
        self.__prestamo=None
        self.__fecha_entrega_real=fecha_entrega_real
        self.__dias_retraso=None
        self.__dias_multa=dias_multa
        self.__fecha_inicio_multa=fecha_inicio_multa
        self.__fecha_final_multa=fecha_final_multa
        self.__activa=activa
        Multa.instancias.append(self)
    
    #getters
    def get_id_multa(self):
        return self.__id_multa
    def get_lector(self):
        return self.__lector
    def get_prestamo(self):
        return self.__prestamo
    def get_fecha_entrega_real(self):
        return self.__fecha_entrega_real
    def get_dias_retraso(self):
        return self.__dias_retraso
    def get_dias_multa(self):
        return self.__dias_multa
    def get_fecha_inicio_multa(self):
        return self.__fecha_inicio_multa
    def get_fecha_final_multa(self):
        return self.__fecha_final_multa
    def get_activa(self):
        return self.__activa
    
    #setters
    def set_id_multa(self,id_multa):
        self.__id_multa=id_multa
    def set_lector(self,lector):
        self.__lector=lector
    def set_prestamo(self,prestamo):
        self.__prestamo=prestamo
    def set_fecha_entrega_real(self,fecha_entrega_real):
        self.__fecha_entrega_real=fecha_entrega_real
    def set_dias_retraso(self,dias_retraso):
        self.__dias_retraso=dias_retraso
    def set_dias_multa(self,dias_multa):
        self.__dias_multa=dias_multa
    def set_fecha_inicio_multa(self,fecha_inicio_multa):
        self.__fecha_inicio_multa=fecha_inicio_multa
    def set_fecha_final_multa(self,fecha_final_multa):
        self.__fecha_final_multa=fecha_final_multa
    def set_activa(self,activa):
        self.__activa=activa
    
    def generar_multa(id_prestamo,fecha_entrega_estimado,fecha_entrega_real):
        # Una multa se asocia sólo a un préstamo, y un préstamo sólo puede tener una multa asociada.
        for multa in Multa._instancias:
            if multa.get_prestamo().get_id_prestamo() == id_prestamo:
                print("Ya existe una multa asociada a este préstamo.")
                return
        
        id_multa=len(Multa.instancias)+1
        prestamo=Prestamo.buscar_prestamo(id_prestamo)
        
        if not prestamo:
            print("Prestamo no encontrado")
            return
        if prestamo.get_activo()==False:
            print("El prestamo ya fue entregado")
            return
        

        lector=prestamo.get_lector()
        dias_retraso=diferencia_fechas(fecha_entrega_estimado, fecha_entrega_real)
        dias_multa=Multa.calcular_multa(dias_retraso)
        fecha_inicio_multa=fecha_entrega_real.sumar_dias(1)
        fecha_fin_multa=fecha_inicio_multa.sumar_dias(dias_multa)
        
        #se crea la multa
        Multa=(id_multa,lector,fecha_entrega_real,dias_retraso,fecha_inicio_multa,fecha_fin_multa).asociar_prestamo(prestamo)
        prestamo.set_activo(False)
        #se debe pasar el lector a estado sancionado
        
        
    def asociar_prestamo(self,prestamo):
        # Se verifica que el préstamo sea una inst  ancia de la clase Prestamo
        if not isinstance(prestamo, Prestamo):
            raise TypeError("El objeto asociado no es un préstamo.")
        # Se asocia el préstamo a la multa
        self.__prestamo = prestamo
        
    def calcular_multa(dias_retraso):
        return dias_retraso*Multa.MULTA_DIAS
        
    def levantar_multa(self):
        self.__activa=False
    
    
    
    def consultar_multas(id_lector):
        lector = Lector.buscar_lector_por_id(id_lector)
        if not lector:
            print("Lector no encontrado")
            return

        print(f"---Préstamos realizados por: {lector.get_nombre()}")

        for prestamo in Prestamo.instancias:
            if prestamo.get_id_lector() == id_lector:
                prestamo.consultar()

        