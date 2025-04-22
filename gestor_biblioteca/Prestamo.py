from gestor_biblioteca.share import *
from gestor_biblioteca.Copia import Copia
from gestor_biblioteca.ArticuloCientifico import ArticuloCientifico
from gestor_biblioteca.Tesis import Tesis
from gestor_biblioteca.Lector import Lector
import random

# -NOTA 20/04/2025 23:02: Falta revisar e integrar correctamente la función de devolución en los menús

def menu_prestamo():
    band=False
    while(not band):
        clear_console()
        
        opcion=pedir_entero("--- Menú Préstamo ---\n\n1) Registrar Préstamo\n2) Consultar Préstamo\n3) Cancelar Préstamo\n4) Consultar productos en préstamo de un lector\n5) Devolución de Préstamo\n0) Salir\n\nSeleccione una opción: ", True)
        clear_console()
        
        if(opcion==1):
            # print("--- Registrar Préstamo ---\n")
            Prestamo.registrar()
            
        elif(opcion==2):
            opcion2=pedir_entero("--- Consultar Préstamo ---\n\n1) Ver lista de préstamos registrados\n2) Consultar préstamo por ID\n0) Salir\n\nSeleccione una opción: ", True)
            clear_console()

            if opcion2 == 1:
                print("--- Lista de préstamos registrados ---\n")
                Prestamo.mostrar_prestamos()

            elif opcion2 == 2:
                id=pedir_entero("--- Consultar Préstamo por ID ---\n\nIngrese el ID del préstamo a consultar: ", True)
                prestamo=Prestamo.buscar_prestamo(id)
                if prestamo == None:
                    clear_console()
                    print(f"No se encontró el préstamo con ID {id}.")
                    esperar()
                    continue
                clear_console()
                print("Préstamo seleccionado:\n")
                Prestamo.consultar(prestamo)
        
        elif(opcion==3):
            print("--- Cancelar Préstamo ---\n")
            id=pedir_entero("Ingrese el ID del préstamo a cancelar: ")
            prestamo=Prestamo.buscar_prestamo(id)
            if prestamo == None:
                clear_console()
                print(f"No se encontró el préstamo con ID {id}.")
                esperar()
                continue
            clear_console()
            Prestamo.cancelar(prestamo)

        elif(opcion==4):
            print("--- Consultar productos en préstamo de un lector ---\n")
            id_lector = input("Ingrese el ID del lector a consultar: ")
            Prestamo.consultar_productos_en_prestamo(id_lector)

        elif(opcion==5):
            print("--- Devolución de Préstamo ---\n")
            id_lector = input("Ingrese el ID del lector que desea devolver un préstamo: ")
            Prestamo.devolucion(id_lector)

        elif(opcion==0):
            band=True
        
        else:
            clear_console()
            print("Opción no válida. Por favor intente nuevamente.")
            esperar()

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
        # Inicialmente no hay producto ni lector asociados
        self.producto = None
        self.lector = None
        # Se agrega la instancia a la lista de préstamos
        Prestamo._instancias.append(self)
    

    def asociar_lector(self, lector):
        # Se verifica que el lector sea una instancia de la clase Lector
        if not isinstance(lector, Lector):
            raise TypeError("El objeto asociado no es un lector.")
        # Se asocia el lector al préstamo
        self.lector = lector

    def asociar_producto(self, producto):
        # Se verifica que el producto sea una copia, artículo científico o tesis
        if not isinstance(producto, Copia) and not isinstance(producto, ArticuloCientifico) and not isinstance(producto, Tesis):
            raise TypeError("El objeto asociado no es un producto.")
        # Se asocia la copia al préstamo
        self.producto = producto

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
    def get_producto(self):
        return self.producto
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
    def mostrar_prestamos(cls):
        """Muestra todos los préstamos registrados."""
        if len(cls._instancias) == 0:
            print("No hay préstamos registrados.")
            esperar()
        else:
            for i in range(len(cls._instancias)):
                print(f" - ID: {cls._instancias[i].get_id_prestamo()} - Nombre Lector: \"{cls._instancias[i].get_lector().get_nombre()}\" - Tipo de producto: \"{cls._instancias[i].get_tipo_producto()}\"")
            esperar()

    @classmethod
    def buscar_prestamo(cls, id_prestamo):
        for prestamo in cls._instancias:
            if prestamo.get_id_prestamo() == id_prestamo:
                return prestamo
        return None
    
    @classmethod
    def obtener_prestamos_activos(cls, lector):
        """Devuelve una lista de préstamos activos asociados a un lector."""
        prestamos_activos = []
        for prestamo in cls._instancias:
            if prestamo.get_lector() == lector and prestamo.get_activo():
                prestamos_activos.append(prestamo)
        return prestamos_activos
    
    @classmethod
    def verificar_lector_elegible(cls, lector):
        """Verifica si un lector es elegible para un préstamo."""
        # Se verifica que el lector sea una instancia de la clase Lector
        if lector is None:
            # print("Lector no encontrado.")
            return False
        
        # Se verifica que el lector no esté inactivo
        if lector.get_estado() == "Inactivo":
            # print("El lector está inactivo y no puede realizar préstamos.")
            return False
        
        # Se verifica que el lector no esté suspendido
        if lector.get_estado() == "Suspendido":
            # print("El lector está suspendido y no puede realizar préstamos.")
            return False
        
        # Se verifica que el lector no esté sancionado (con multa activa)
        if lector.get_estado() == "Sancionado":
            # print("El lector está sancionado y no puede realizar préstamos.")
            return False
        
        # Se verifica que el lector no tenga más del máximo de préstamos activos permitido
        prestamos_activos_lector = len(cls.obtener_prestamos_activos(lector))
        
        # Se define el máximo de préstamos por lector
        # (Este valor puede ser ajustado según las políticas de la biblioteca)
        MAX_PRESTAMOS_POR_LECTOR = 3
        
        if prestamos_activos_lector >= MAX_PRESTAMOS_POR_LECTOR:
            # print(f"El lector ya tiene {MAX_PRESTAMOS_POR_LECTOR} préstamos activos.")
            return False
        
        return True
    
    def registrar():
        while True:
            clear_console()
            print("--- Registrar Préstamo ---\n")
            id_prestamo = pedir_entero("Ingrese el ID del préstamo (deje en blanco para una asignación automática): ", False, True)
            if id_prestamo is None:
                # Generar ID aleatorio de 7 dígitos
                id_prestamo = random.randint(1000000, 9999999)
                # Verificar si el ID ya existe
                if Prestamo.buscar_prestamo(id_prestamo) is None:
                    break
            else:
                if Prestamo.buscar_prestamo(id_prestamo) is not None:
                    clear_console()
                    print("ID ya registrado. Pruebe con otro valor.")
                    esperar()
                else:
                    break
        
        id_lector = input("Ingrese el ID del lector asociado: ")
        lector = Lector.buscar_lector(id_lector)
        # Se verifica que el lector sea elegible para el préstamo
        if not Prestamo.verificar_lector_elegible(lector) and lector is not None:
            clear_console()
            print("No se pudo registrar el préstamo: Lector no elegible.")
            esperar()
            return

        if lector is None:
            clear_console()
            print(f"No se pudo registrar el préstamo: Lector con ID {id_lector} no encontrado.")
            esperar()
            return
        
        band = False
        while band == False:
            clear_console()
            opcion = pedir_entero("--- ¿Qué tipo de producto desea asociar? ---\n\n1) Copia de libro\n2) Artículo científico\n3) Tesis\n\nSeleccione una opción: ", True)
            clear_console()
            if opcion == 1:
                tipo_producto = "Copia de libro"
                band = True
            elif opcion == 2:
                tipo_producto = "Artículo científico"
                band = True
            elif opcion == 3:
                tipo_producto = "Tesis"
                band = True
           
            else:
                clear_console()
                print("Opción no válida. Intente nuevamente.")
                esperar()
                
        clear_console()
        print(f"--- Registrar Préstamo ---\n\nId Préstamo: {id_prestamo}\nID Lector: {lector.get_id_lector()}\nTipo de producto: {tipo_producto}\n")
            
        if opcion == 1:
            id_prod = pedir_entero("Ingrese el ID de la copia asociada: ")
            producto = Copia.buscar_copia(id_prod)
            if producto is None:
                clear_console
                print(f"No se pudo registrar el préstamo: Copia con ID {id_prod} no encontrada.")
                esperar()
                return
            else:
                # Se verifica que la copia esté disponible
                if producto.get_estado() != "Disponible":
                    clear_console()
                    print(f"No se pudo registrar el préstamo: La copia con ID {id_prod} no está disponible.")
                    esperar()
                    return
                
        elif opcion == 2:
            id_prod = input("Ingrese el DOI del artículo científico asociado: ")
            producto = ArticuloCientifico.buscar_articulo(id_prod)
            if producto is None:
                clear_console()
                print(f"No se pudo registrar el préstamo: Artículo científico con DOI \"{id_prod}\" no encontrado.")
                esperar()
                return
            else:
                # Se verifica que el artículo esté disponible
                if producto.get_estado() != "Disponible":
                    clear_console()
                    print(f"No se pudo registrar el préstamo: El artículo científico con DOI \"{id_prod}\" no está disponible.")
                    esperar()
                    return
                
        elif opcion == 3:
            id_prod = pedir_entero("Ingrese el ID de la tesis asociada: ")
            producto = Tesis.buscar_tesis(id_prod)
            if producto is None:
                clear_console()
                print(f"No se pudo registrar el préstamo: Tesis con ID {id_prod} no encontrada.")
                esperar()
                return
            else:
                # Se verifica que la tesis esté disponible
                if producto.get_estado() != "Disponible":
                    clear_console()
                    print(f"No se pudo registrar el préstamo: La tesis con ID {id_prod} no está disponible.")
                    esperar()
                    return
        
        clear_console()
        if opcion == 1:
            print(f"--- Registrar Préstamo ---\n\nId Préstamo: {id_prestamo}\nID Lector: {lector.get_id_lector()}\nID Copia: {producto.get_id_copia()}\n")
        elif opcion == 2:
            print(f"--- Registrar Préstamo ---\n\nId Préstamo: {id_prestamo}\nID Lector: {lector.get_id_lector()}\nDOI Artículo: \"{producto.get_doi()}\"\n")
        elif opcion == 3: 
            print(f"--- Registrar Préstamo ---\n\nId Préstamo: {id_prestamo}\nID Lector: {lector.get_id_lector()}\nID Tesis: {producto.get_idTesis()}\n")
        
        print("A continuación ingrese la fecha de préstamo.")
        fecha_prestamo = Date.registrar_fecha()
        dias_prestamo = pedir_entero("Ingrese la cantidad de días de préstamo: ")
        # Se verifica que los días no sean superiores a 30
        if dias_prestamo > 30:
            clear_console()
            print("No se puede registrar un préstamo por más de 30 días.")
            esperar()
            return
        
        # Se verifica que los días no sean negativos
        if dias_prestamo < 0:
            clear_console()
            print("No se puede registrar un préstamo por menos de 0 días.")
            esperar()
            return
        
        fecha_entrega_estimada = fecha_prestamo.sumar_dias(dias_prestamo)
        activo = True

        # Se crea el préstamo y se asocian la copia y el lector
        prestamo = Prestamo(id_prestamo, tipo_producto, dias_prestamo, fecha_prestamo, fecha_entrega_estimada, activo)
        prestamo.asociar_lector(lector)
        prestamo.asociar_producto(producto)

        # Se actualiza el estado del producto
        if isinstance(producto, Copia):
            producto.set_estado("Prestada")
        else:
            producto.set_estado("Prestado")
        
        clear_console()
        print(f"Préstamo con ID {prestamo.get_id_prestamo()} registrado con éxito.")
        esperar()


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
        if self.producto is not None:
            if self.tipo_producto == "Copia de libro":
                print(f"ID de copia asociada: {self.producto.get_id_copia()}")
            elif self.tipo_producto == "Artículo científico":
                print(f"DOI de artículo asociado: \"{self.producto.get_doi()}\"")
            elif self.tipo_producto == "Tesis":
                print(f"ID de tesis asociada: {self.producto.get_idTesis()}")
        if self.lector is not None:
            print(f"ID de lector asociado: {self.lector.get_id_lector()}")

        esperar()

    def finalizar(self):
        """Finaliza el préstamo y actualiza el estado de la copia y el lector."""
        if self.producto is not None:
            self.producto.set_estado("Disponible")
        if self.lector is not None:
            self.lector.set_estado("Normal")
        self.activo = False
        print(f"Préstamo con ID {self.id_prestamo} finalizado con éxito.")

    def cancelar(self):
        """Cancela el préstamo y actualiza el estado de la copia y el lector."""
        if self.producto is not None:
            self.producto.set_estado("Disponible")
        if self.lector is not None:
            self.lector.set_estado(self.lector.get_estado_previo())
        self.activo = False
        print(f"Préstamo con ID {self.id_prestamo} cancelado con éxito.")

    def consultar_productos_en_prestamo(id_lector):
        """Consulta los productos en préstamo de un lector."""
        lector = Lector.buscar_lector(id_lector)
        if lector is None:
            clear_console()
            print("Lector no encontrado.")
            esperar()
            return
        prestamos = [prestamo for prestamo in Prestamo._instancias if prestamo.get_lector() == lector and prestamo.get_activo()]
        if prestamos:
            clear_console()
            print(f"--- Productos en préstamo del lector {lector.get_id_lector()} ---\n")
            for prestamo in prestamos:
                prestamo.consultar()
            esperar()

        else:
            clear_console()
            print(f"No hay productos en préstamo para el lector {lector.get_id_lector()}.")
            esperar()

    def devolucion(id_lector):
        """
        Realiza la devolución de un préstamo asociado a un lector.

        Parámetros:
        -----------
        id_lector : int
            El ID del lector que desea devolver un préstamo.

        Descripción:
        ------------
        Esta función permite realizar la devolución de un préstamo activo asociado a un lector. 
        Primero, busca al lector por su ID. Si el lector no existe, muestra un mensaje de error.
        Luego, busca los préstamos activos asociados al lector. Si hay préstamos activos, 
        muestra una lista de ellos y permite al usuario seleccionar cuál desea devolver.

        Durante la devolución:
        - Se solicita la fecha de entrega real.
        - Se genera una multa si la devolución se realiza después de la fecha estimada de entrega.
        - Se finaliza el préstamo y se actualizan los estados correspondientes.

        Si no hay préstamos activos asociados al lector, se muestra un mensaje informativo.

        Flujo de la función:
        --------------------
        1. Buscar al lector por su ID.
        2. Verificar si el lector tiene préstamos activos.
        3. Mostrar una lista de préstamos activos y permitir al usuario seleccionar uno.
        4. Solicitar la fecha de entrega real.
        5. Generar una multa si corresponde.
        6. Finalizar el préstamo y actualizar los estados.
        7. Mostrar mensajes informativos en caso de errores o acciones completadas.

        Excepciones:
        ------------
        - Si el lector no existe, se muestra "Lector no encontrado."
        - Si no hay préstamos activos, se muestra "No hay préstamos activos asociados al lector."
        - Si el usuario selecciona una opción inválida, se muestra "Opción no válida. Intente nuevamente."

        Ejemplo de uso:
        ---------------
        devolucion(12345)
        """
        
        from gestor_biblioteca.Multa import Multa
    
        lector = Lector.buscar_lector(id_lector)
        if lector is None:
            clear_console()
            print("Lector no encontrado.")
            esperar()
            return
        
        # Se busca el préstamo asociado al lector
        prestamos_activos = Prestamo.obtener_prestamos_activos(lector)
        if prestamos_activos:
            while True:
                clear_console()
                print(f"--- Prestamos activos para el lector con ID {lector.get_id_lector()} ---\n")
                print("0) Salir")
                for i in range(len(prestamos_activos)):
                    tipo_producto = prestamos_activos[i].get_tipo_producto()
                    if tipo_producto == "Copia de libro":
                        print(f"{i+1}) ID Préstamo: {prestamos_activos[i].get_id_prestamo()} - ID Copia: {prestamos_activos[i].get_producto().get_id_copia()}")
                    elif tipo_producto == "Artículo científico":
                        print(f"{i+1}) ID Préstamo: {prestamos_activos[i].get_id_prestamo()} - DOI Artículo: \"{prestamos_activos[i].get_producto().get_doi()}\"")
                    elif tipo_producto == "Tesis":
                        print(f"{i+1}) ID Préstamo: {prestamos_activos[i].get_id_prestamo()} - ID Tesis: {prestamos_activos[i].get_producto().get_idTesis()}")
                
                opcion = pedir_entero("\nSeleccione el préstamo a devolver: ") - 1
                if opcion == -1:
                    break
                elif 0 <= opcion < len(prestamos_activos):
                    prestamo = prestamos_activos[opcion]
                    # Se verifica que el préstamo esté activo
                    if prestamo.get_activo():
                        print("A continuación ingrese la fecha de entrega real.")
                        fecha_entrega_real = Date.registrar_fecha()
                        if not Multa.generar_multa(prestamo.get_id_prestamo(), prestamo.get_fecha_entrega_estimada(), fecha_entrega_real):
                            prestamo.finalizar()
                        esperar()
                        return
                    else:
                        clear_console()
                        print("El préstamo ya ha sido finalizado.")
                        esperar()
                        return
                else:
                    clear_console()
                    print("Opción no válida. Intente nuevamente.")
                    esperar()
        else:
            print("No hay préstamos activos asociados al lector.")
            esperar()
