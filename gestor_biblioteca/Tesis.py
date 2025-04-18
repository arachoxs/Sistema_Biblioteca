from gestor_biblioteca.share import *
from gestor_biblioteca.Categoria import Categoria

class Tesis:
    _instancias = []

    def __init__(self, idTesis, nombre, institucion, fechaInvestigacion, fechaPrestacion, campoEstudio, nPaginas, estado = "Disponible"):
        self.__idTesis = idTesis
        self.__nombre = nombre
        self.__institucion = institucion
        self.__fechaInvestigacion = fechaInvestigacion
        self.__fechaPrestacion = fechaPrestacion
        self.__campoEstudio = campoEstudio
        self.__nPaginas = nPaginas
        self.__estado = estado

        self.__categoria_tesis = None

        Tesis._instancias.append(self)

    #getters
    def get_idTesis(self):
        return self.__idTesis
    def get_nombre(self):
        return self.__nombre
    def get_institucion(self):
        return self.__institucion
    def get_fechaInvestigacion(self):
        return self.__fechaInvestigacion
    def get_fechaPrestacion(self):
        return self.__fechaPrestacion
    def get_campoEstudio(self):
        return self.__campoEstudio
    def get_nPaginas(self):
        return self.__nPaginas
    def get_estado(self):
        return self.__estado
    def get_categoria_tesis(self):
        return self.__categoria_tesis
    
    #setters
    def set_idTesis(self, idTesis):
        self.__idTesis = idTesis
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_institucion(self, institucion):
        self.__institucion = institucion
    def set_fechaInvestigacion(self, fechaInvestigacion):
        self.__fechaInvestigacion = fechaInvestigacion
    def set_fechaPrestacion(self, fechaPrestacion):
        self.__fechaPrestacion = fechaPrestacion
    def set_campoEstudio(self, campoEstudio):
        self.__campoEstudio = campoEstudio
    def set_nPaginas(self, nPaginas):
        self.__nPaginas = nPaginas
    def set_estado(self, estado):
        self.__estado = estado

    #metodos
    def registrar():
        idTesis = pedir_entero("Ingrese el id de la tesis: ")
        nombre = input("Ingrese el nombre de la tesis: ")   
        institucion = input("Ingrese la institucion de la tesis: ")

        fechaInvestigacion = Date.registrar_fecha()
        fechaPrestacion = Date.registrar_fecha()

        campoEstudio = input("Ingrese el campo de estudio de la tesis: ")
        nPaginas = pedir_entero("Ingrese el numero de paginas de la tesis: ")

        Tesis(idTesis, nombre, institucion, fechaInvestigacion, fechaPrestacion, campoEstudio, nPaginas)
        Tesis.asignar_categoria()
    
    def consultar(self):
        print("ID Tesis: ", self.__idTesis)
        print("Nombre: ", self.__nombre)
        print("Institucion: ", self.__institucion)
        print("Fecha de investigacion: ", self.__fechaInvestigacion)
        print("Fecha de prestacion: ", self.__fechaPrestacion)
        print("Campo de estudio: ", self.__campoEstudio)
        print("Numero de paginas: ", self.__nPaginas)
        print("Estado: ", self.__estado)

        if (self.__categoria_tesis == None):
            print("No se ha asignado categoria a la tesis.")
        else:
            print("Categoria de la tesis: ", self.__categoria_tesis.get_nombre())

    def modificar(self):
        print("---Tesis seleccionada---")
        self.consultar()
        band=True
        while band:
            print("¿Qué desea modificar?")
            print("0. Salir")
            print("1. ID Tesis")
            print("2. Nombre")
            print("3. Institucion")
            print("4. Fecha de investigacion")
            print("5. Fecha de prestacion")
            print("6. Campo de estudio")
            print("7. Numero de paginas")
            print("8. Estado")
            print("9. Categoria")


            opcion = pedir_entero("Ingrese la opcion: ")

            if opcion == 1:
                idTesis = pedir_entero("Ingrese el nuevo id de la tesis: ")
                self.set_idTesis(idTesis)
                print("ID Tesis modificado con exito.")
            elif opcion == 2:
                nombre = input("Ingrese el nuevo nombre de la tesis: ")
                self.set_nombre(nombre)
                print("Nombre modificado con exito.")
            elif opcion == 3:
                institucion = input("Ingrese la nueva institucion de la tesis: ")
                self.set_institucion(institucion)
                print("Institucion modificada con exito.")
            elif opcion == 4:
                fechaInvestigacion = Date.registrar_fecha()
                self.set_fechaInvestigacion(fechaInvestigacion)
                print("Fecha de investigación modificada con exito.")
            elif opcion == 5:
                fechaPrestacion= Date.registrar_fecha()
                self.set_fechaPrestacion(fechaPrestacion)
                print("Fecha de prestación modificada con exito.")	
            elif opcion == 6:
                campoEstudio = input("Ingrese el nuevo campo de estudio de la tesis: ")
                self.set_campoEstudio(campoEstudio)
                print("Campo de estudio modificado con exito.")
            elif opcion == 7:
                nPaginas = pedir_entero("Ingrese el nuevo numero de paginas de la tesis: ")
                self.set_nPaginas(nPaginas)
                print("Numero de paginas modificado con exito.")
            elif opcion == 8:
                print("Seleccione el estado de la Tesis:")
                print("1. Disponible")
                print("2. Prestado")
                print("3. En revisión")
                print("4. En reparación")
                print("5. No disponible")
                
                opcionEstado = pedir_entero("Ingrese la opción: ")
                
                if opcionEstado == 1:
                    estado = "Disponible"
                elif opcionEstado == 2:
                    estado = "Prestado"
                elif opcionEstado == 3:
                    estado = "En revisión"
                elif opcionEstado == 4:
                    estado = "En reparación"
                elif opcionEstado == 5:
                    estado = "No disponible"
                else:
                    print("Opción inválida. No se modificó el estado.")
                    return
                self.set_estado(estado)
                print("Estado modificado con exito.")
            elif opcion == 9:
                self.asignar_categoria()
            elif opcion == 0:
                band = False
                print("Saliendo de la modificación de la Tesis...")
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def eliminar(self):
        print("---Tesis seleccionada---")
        self.consultar()

        respuesta = input("¿Está seguro de que desea eliminar la tesis? (s/n): ")

        if respuesta.lower() == "s":
            Tesis._instancias.remove(self)
            print("Tesis eliminada con exito.")
        else:
            print("Eliminacion cancelada.")
       
def asignar_categoria(self):
    band = True
    if self.__estado == "No disponible":
        print("No se puede asignar categoria a una tesis No disponible.")
        return
    if len(Categoria.obtener_instancias()) == 0:
        print("No hay categorias disponibles para asignar.")
        return
    while band:
        print("Categorias disponibles:")
        for index in range(len(Categoria.obtener_instancias())):
            print(index + 1, ". ", Categoria.obtener_instancias()[index].get_nombre())

        opcion = pedir_entero("Seleccione una categoria: ")
        opcion -= 1

        if opcion >= 0 and opcion < len(Categoria.obtener_instancias()):
            self.__categoria_tesis = Categoria.obtener_instancias()[opcion]
            print("Categoria asignada con exito.")
            band = False
        else:
            print("Opcion no valida, intente nuevamente.")

