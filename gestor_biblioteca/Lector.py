class Lector:
    _instancias = []

    def __init__(self, id_lector, nombre, telefono, direccion, estado = "Normal"):
        # Atributos del lector
        self.id_lecto = id_lector
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.estado = estado
        # Se agrega la instancia a la lista de lectores
        Lector._instancias.append(self)

    # Getters
    def get_id_lector(self):
        return self.id_lecto
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
        self.id_lecto = id_lector
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

    def registrar():
        while True:
            id_lector = input("Ingrese el ID del lector: ")
            if Lector.buscar_lector(id_lector) is None:
                break
            print("ID ya registrado. Intente nuevamente.")
        nombre = input("Ingrese el nombre del lector: ")
        telefono = input("Ingrese el telefono del lector: ")
        direccion = input("Ingrese la direccion del lector: ")
        estado = "Normal"

        Lector(id_lector, nombre, telefono, direccion, estado)
        print(f"Lector con ID {id_lector} registrado con exito.")

    def consultar(self):
        print(f"ID: {self.id_lector}")
        print(f"Nombre: {self.nombre}")
        print(f"Telefono: {self.telefono}")
        print(f"Direccion: {self.direccion}")
        print(f"Estado: {self.estado}")

    def modificar(self):
        if self.estado == "Inactivo":
            print("No se puede modificar un lector inactivo.")
        else:
            print("Ingrese los nuevos datos del lector (deje en blanco para no modificar):")
            id_lector = input(f"ID ({self.id_lector}): ")
            nombre = input(f"Nombre ({self.nombre}): ")
            telefono = input(f"Telefono ({self.telefono}): ")
            direccion = input(f"Direccion ({self.direccion}): ")
            print("Estado (seleccione una opción):\n1. Normal\n2. Sancionado\n3. Suspendido")
            estado = input(f"Estado ({self.estado}): ")
            if estado == "1":
                estado = "Normal"
            elif estado == "2":
                estado = "Sancionado"
            elif estado == "3":
                estado = "Suspendido"
            else:
                estado = self.estado

            if id_lector:
                self.set_id_lector(id_lector)
            if nombre:
                self.set_nombre(nombre)
            if telefono:
                self.set_telefono(telefono)
            if direccion:
                self.set_direccion(direccion)
            if estado:
                self.set_estado(estado)

            print("Lector modificado con exito.")

    def inhabilitar(self):
        self.set_estado("Inactivo")
        print(f"Lector con ID {self.id_lector} inhabilitado.")

    def habilitar(self):
        self.set_estado("Normal")
        print(f"Lector con ID {self.id_lector} habilitado.")

    def sancionar(self):
        self.set_estado("Sancionado")
        print(f"Lector con ID {self.id_lector} sancionado.")
    
    def suspender(self):
        self.set_estado("Suspendido")
        print(f"Lector con ID {self.id_lector} suspendido.")

    def obtener_lectores():
        return Lector._instancias.deepcopy()
    
    