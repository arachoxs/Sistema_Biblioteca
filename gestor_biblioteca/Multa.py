from gestor_biblioteca.share import *
from gestor_biblioteca.Prestamo import Prestamo
from gestor_biblioteca.Lector import Lector


def menu_multa():
    band = False
    while not band:
        clear_console()

        opcion = pedir_entero("--- Menú Multa ---\n\n1) Generar Multa\n2) Consultar Multas\n3) Levantar Multas Automáticamente\n0) Salir\n\nSeleccione una opción: ", True)
        clear_console()

        if opcion == 1:
            print("--- Generar Multa ---\n")
            id_prestamo = pedir_entero("Ingrese el ID del préstamo: ")
            prestamo = Prestamo.buscar_prestamo(id_prestamo)
            if prestamo is None:
                clear_console()
                print(f"No se encontró el préstamo con ID {id_prestamo}.")
                esperar()
                continue
            
            if prestamo.get_activo() == False:
                clear_console()
                print(f"El préstamo con ID {id_prestamo} ya fue entregado.")
                esperar()
                continue

            fecha_entrega_estimada = prestamo.get_fecha_entrega_estimada()
            print("---Ingrese la fecha de entrega real---")
            fecha_entrega_real = Date.registrar_fecha()
            Multa.generar_multa(id_prestamo, fecha_entrega_estimada, fecha_entrega_real)

        elif opcion == 2:
            opcion2=pedir_entero("--- Consultar multas lectores ---\n\n1) Ver lista de multas\n2) Consultar multa por ID\n0) Salir\n\nSeleccione una opción: ", True)
            clear_console()

            if opcion2 == 1:
                print("--- Lista de multas registradas ---\n")
                Multa.mostrar_multas()
                esperar()

            elif opcion2 == 2:
                id=input("--- Consultar multa por ID ---\n\nIngrese el ID de la multa a consultar: ")
                multa = multa.buscar_multa(id)
                if multa == None:
                    clear_console()
                    print(f"No se encontró la multa con ID \"{id}\".")
                    esperar()
                    continue
                clear_console()
                print("Multa seleccionada:\n")
                multa.consultar()
                esperar()

        elif opcion == 3:
            print("---Ingrese la fecha actual---")
            fecha = Date.registrar_fecha()
            Multa.levantar_multas_auto(fecha)

        elif opcion == 0:
            band = True

        else:
            print("Opción no válida. Por favor intente nuevamente.")
            esperar()


class Multa:
    _instancias = []  # Lista para almacenar todas las instancias de multas
    MULTA_DIAS = 3  # Días de sanción por cada día de retraso

    def __init__(self, id_multa, lector, fecha_entrega_real, dias_retraso, dias_multa, fecha_inicio_multa, fecha_final_multa, activa=True):
        self.__id_multa = id_multa
        self.__lector = lector
        self.__prestamo = None
        self.__fecha_entrega_real = fecha_entrega_real
        self.__dias_retraso = dias_retraso
        self.__dias_multa = dias_multa
        self.__fecha_inicio_multa = fecha_inicio_multa
        self.__fecha_final_multa = fecha_final_multa
        self.__activa = activa
        Multa._instancias.append(self)

    # Getters
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

    # Setters
    def set_prestamo(self, prestamo):
        if not isinstance(prestamo, Prestamo):
            raise TypeError("El objeto asociado no es un préstamo.")
        self.__prestamo = prestamo

    def set_activa(self, activa):
        self.__activa = activa

    @staticmethod
    def calcular_multa(dias_retraso):
        """Calcula los días de sanción en función de los días de retraso."""
        return dias_retraso * Multa.MULTA_DIAS

    @staticmethod
    def generar_multa(id_prestamo, fecha_entrega_estimado, fecha_entrega_real):
        """Genera una multa asociada a un préstamo."""
        # Verificar si ya existe una multa para el préstamo
        for multa in Multa._instancias:
            if multa.get_prestamo() and multa.get_prestamo().get_id_prestamo() == id_prestamo:
                print("Ya existe una multa asociada a este préstamo.")
                return False

        prestamo = Prestamo.buscar_prestamo(id_prestamo)
        if not prestamo:
            print("Préstamo no encontrado.")
            return False

        if not prestamo.get_activo():
            print("El préstamo ya fue entregado.")
            return False

        lector = prestamo.get_lector()
        diferencia = diferencia_fechas(fecha_entrega_estimado, fecha_entrega_real)

        if diferencia <= 0:
            print("No hay retraso; no se genera multa.")
            return False

        dias_multa = Multa.calcular_multa(diferencia)
        fecha_inicio_multa = fecha_entrega_real.sumar_dias(1)
        fecha_fin_multa = fecha_inicio_multa.sumar_dias(dias_multa)

        # Crear la multa
        id_multa = len(Multa._instancias) + 1
        multa = Multa(id_multa, lector, fecha_entrega_real, diferencia, dias_multa, fecha_inicio_multa, fecha_fin_multa)
        multa.set_prestamo(prestamo)
        prestamo.finalizar()
        lector.sancionar()

        print(f"Multa generada exitosamente con ID {id_multa}.")
        return True

    def levantar_multa(self):
        """Levanta la multa y habilita al lector."""
        self.__activa = False
        lector = self.__prestamo.get_lector()
        lector.habilitar()
        print(f"Multa {self.__id_multa} levantada.")

    @staticmethod
    def levantar_multas_auto(fecha_actual):
        """Levanta automáticamente las multas que hayan cumplido su periodo."""
        for multa in Multa._instancias:
            if multa.get_activa() and fecha_actual >= multa.get_fecha_final_multa():
                multa.levantar_multa()
    def mostrar_multas():
        if len(Multa._instancias) == 0:
            print("No hay multas registradas.")
            esperar()
            return 
        
        for i in len(Multa._instancias):
            print(f"{1})-ID Multa: {Multa._instancias[i].get_id_multa()} -ID Prestamo: {Multa._instancias[i].get_prestamo().get_id_prestamo()} - Nombre Lector: {Multa._instancias[i].get_lector().get_nombre()} - Fecha de entrega real: {Multa._instancias[i].get_fecha_entrega_real()} - fecha de entrega estimada: {Multa._instancias[i].get_prestamo().get_fecha_entrega_estimada()} - Activa: {Multa._instancias[i].get_activa()}")

    def buscar_multa(id):
        for multa in Multa._instancias:
            if multa.get_id_multa() == id:
                return multa
        return None 
    
    def consultar(self):
        """Consulta los detalles de la multa."""
        print(f"ID Multa: {self.get_id_multa()}")
        print(f"ID Préstamo: {self.get_prestamo().get_id_prestamo()}")
        print(f"ID Lector: {self.get_lector().get_id_lector()}")
        print(f"Nombre Lector: {self.get_lector().get_nombre()}")
        print(f"Fecha de entrega real: {self.get_fecha_entrega_real()}")
        print(f"Días de retraso: {self.get_dias_retraso()}")
        print(f"Días de multa: {self.get_dias_multa()}")
        print(f"Fecha inicio multa: {self.get_fecha_inicio_multa()}")
        print(f"Fecha fin multa: {self.get_fecha_final_multa()}")
        print(f"Activa: {'Sí' if self.get_activa() else 'No'}")

    @staticmethod
    def consultar_multas(id_lector):
        """Consulta las multas activas de un lector."""
        lector = Lector.buscar_lector(id_lector)
        if not lector:
            print("Lector no encontrado.")
            return

        print(f"--- Multas activas para: {lector.get_nombre()} ---")
        multas_encontradas = False

        for multa in Multa._instancias:
            if multa.get_prestamo() and multa.get_prestamo().get_lector() == lector and multa.get_activa():
                multas_encontradas = True
                print(f"ID Multa: {multa.get_id_multa()}")
                print(f"ID Préstamo: {multa.get_prestamo().get_id_prestamo()}")
                print(f"Fecha de entrega real: {multa.get_fecha_entrega_real()}")
                print(f"Días de retraso: {multa.get_dias_retraso()}")
                print(f"Días de multa: {multa.get_dias_multa()}")
                print(f"Fecha inicio multa: {multa.get_fecha_inicio_multa()}")
                print(f"Fecha fin multa: {multa.get_fecha_final_multa()}")
                print("------------------------------")

        if not multas_encontradas:
            print("No se encontraron multas activas para este lector.")

