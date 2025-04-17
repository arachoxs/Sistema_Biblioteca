from share import *
from gestor_biblioteca.Prestamo import Prestamo
from gestor_biblioteca.Lector import Lector
class Multa:
    instancias=[]
    MULTA_DIAS=3
    
    
    def __init__(self,id_multa,lector,fecha_entrega_real,dias_multa,fecha_inicio_multa,fecha_final_multa,activa=True):
        self.__id_multa=id_multa
        self.__lector=lector
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
    
    def generar_multa(prestamo,fecha_entrega_estimado,fecha_entrega_real):
        dias_retraso=Date.diferencia_fechas(fecha_entrega_estimado, fecha_entrega_real)
        dias_multa=Multa.calcular_multa(dias_retraso)
        fecha_inicio_multa=Date.sum_dias_fecha(fecha_entrega_real,1)
        fecha_fin_multa=Date.sum_dias_fecha(fecha_inicio_multa,dias_multa)
        
        
        
    def calcular_multa(dias_retraso):
        return dias_retraso*Multa.MULTA_DIAS
        
    def levantar_multa(self):
        self.__activa=False
        
        
    def buscar_lector_por_id(id_lector): #se debe pasar a la clase lector 
        for lector in Lector.instancias:
            if lector.get_id_lector() == id_lector:
                return lector
        return None
    
    def consultar_multas(id_lector):
        lector = Lector.buscar_lector_por_id(id_lector)
        if not lector:
            print("Lector no encontrado")
            return

        print(f"---Préstamos realizados por: {lector.get_nombre()}")

        for prestamo in Prestamo.instancias:
            if prestamo.get_id_lector() == id_lector:
                prestamo.consultar()

        