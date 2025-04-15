class Multa:
    def __init__(self,id_multa,lector,fecha_entrega_real,dias_retraso,dias_multa,fecha_inicio_multa,fecha_final_multa,activa=True):
        self.__id_multa=id_multa
        self.__lector=lector
        self.__fecha_entrega_real=fecha_entrega_real
        self.__dias_retraso=dias_retraso
        self.__dias_multa=dias_multa
        self.__fecha_inicio_multa=fecha_inicio_multa
        self.__fecha_final_multa=fecha_final_multa
        self.__activa=activa
    
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
    
    def registrar(self):
        id_multa = input("Ingrese el ID de la multa: ")
        lector = input("Ingrese el ID del lector: ")
        fecha_entrega_real = input("Ingrese la fecha de entrega real (YYYY-MM-DD): ")
        dias_retraso = int(input("Ingrese los días de retraso: "))
        dias_multa = int(input("Ingrese los días de multa: "))
        fecha_inicio_multa = input("Ingrese la fecha de inicio de la multa (YYYY-MM-DD): ")
        fecha_final_multa = input("Ingrese la fecha final de la multa (YYYY-MM-DD): ")
        activa = True if input("¿La multa está activa? (s/n): ").lower() == 's' else False
        
        return Multa(id_multa,lector,fecha_entrega_real,dias_retraso,dias_multa,fecha_inicio_multa,fecha_final_multa,activa)
        