from gestor_biblioteca.share import *
from gestor_biblioteca.Categoria import Categoria

class ArticuloCientifico:
    _instancias = []

    def __init__(self,doi,titulo,editor,fechaPublicacion,revista,periodicidad,nVolumen,campoInteres,estado = "Disponible"):
        self.__doi = doi
        self.__titulo = titulo
        self.__editor = editor
        self.__fechaPublicacion = fechaPublicacion
        self.__revista = revista
        self.__periodicidad = periodicidad
        self.__nVolumen = nVolumen
        self.__campoInteres = campoInteres
        self.__estado = estado

        self.__categoria_articulo = None

        ArticuloCientifico._instancias.append(self)

    #getters
    def get_doi(self):
        return self.__doi
    def get_titulo(self):
        return self.__titulo
    def get_editor(self):
        return self.__editor
    def get_fechaPublicacion(self):
        return self.__fechaPublicacion
    def get_revista(self):
        return self.__revista
    def get_periodicidad(self):
        return self.__periodicidad
    def get_nVolumen(self):
        return self.__nVolumen
    def get_campoInteres(self):
        return self.__campoInteres
    def get_estado(self):
        return self.__estado
    def get_categoria_articulo(self):
        return self.__categoria_articulo
    
    #setters
    def set_doi(self,doi):
        self.__doi = doi
    def set_titulo(self,titulo):
        self.__titulo = titulo
    def set_editor(self,editor):
        self.__editor = editor
    def set_fechaPublicacion(self,fechaPublicacion):
        self.__fechaPublicacion = fechaPublicacion
    def set_revista(self,revista):
        self.__revista = revista
    def set_periodicidad(self,periodicidad):
        self.__periodicidad = periodicidad
    def set_nVolumen(self,nVolumen):
        self.__nVolumen = nVolumen
    def set_campoInteres(self,campoInteres):
        self.__campoInteres = campoInteres
    def set_estado(self,estado):
        self.__estado = estado

    #metodos
    def registrar():
        doi = input("Ingrese el DOI del articulo: ")
        titulo = input("Ingrese el titulo del articulo: ")
        editor = input("Ingrese el editor del articulo: ")
        
        fechaPublicacion = Date.registrar_fecha()
        
        revista = input("Ingrese la revista del articulo: ")
        periodicidad = input("Ingrese la periodicidad del articulo: ")
        nVolumen = pedir_entero(input("Ingrese el volumen del articulo: "))
        campoInteres = input("Ingrese el campo de interes del articulo: ")

        ArticuloCientifico(doi, titulo, editor, fechaPublicacion, revista, periodicidad, nVolumen, campoInteres)
        ArticuloCientifico.asignar_categoria()


    def consultar(self):
        print("DOI: ", self.__doi)
        print("Titulo: ", self.__titulo)
        print("Editor: ", self.__editor)
        print("Fecha de Publicacion: ", self.__fechaPublicacion)
        print("Revista: ", self.__revista)
        print("Periodicidad: ", self.__periodicidad)
        print("Volumen: ", self.__nVolumen)
        print("Campo de Interes: ", self.__campoInteres)
        print("Estado: ", self.__estado)

        if (self.__categoria_articulo == None):
            print("No se ha asignado una categoría al artículo.")
        else:
            print("Categoría del artículo: ", self.__categoria_articulo.get_nombre())

    def modificar(self):
        print("---Artículo Científico seleccionado---")
        self.consultar()
        band=True
        while band:
            print("¿Qué desea modificar?")
            print("0. Salir")
            print("1. DOI")
            print("2. Titulo")
            print("3. Editor")
            print("4. Fecha de Publicacion")
            print("5. Revista")
            print("6. Periodicidad")
            print("7. Volumen")
            print("8. Campo de Interes")
            print("9. Estado")
            print("10. Categoría")


            opcion = pedir_entero(input("Seleccione una opción: "))

            if opcion == 1:
                doi = input("Ingrese el nuevo DOI del articulo: ")
                self.set_doi(doi)
                print("DOI modificado correctamente.")
            elif opcion == 2:
                titulo = input("Ingrese el nuevo titulo del articulo: ")
                self.set_titulo(titulo)
                print("Titulo modificado correctamente.")
            elif opcion == 3:
                editor = input("Ingrese el nuevo editor del articulo: ")
                self.set_editor(editor)
                print("Editor modificado correctamente.")
            elif opcion == 4:
                fechaPublicacion = Date.registrar_fecha()
                self.set_fechaPublicacion(fechaPublicacion)
                print("Fecha de Publicacion modificada correctamente.")
            elif opcion == 5:
                revista = input("Ingrese la nueva revista del articulo: ")
                self.set_revista(revista)
                print("Revista modificada correctamente.")
            elif opcion == 6:
                periodicidad = input("Ingrese la nueva periodicidad del articulo: ")
                self.set_periodicidad(periodicidad)
                print("Periodicidad modificada correctamente.")
            elif opcion == 7:
                nVolumen = pedir_entero(input("Ingrese el nuevo volumen del articulo: "))
                self.set_nVolumen(nVolumen)
                print("Volumen modificado correctamente.")
            elif opcion == 8:
                campoInteres = input("Ingrese el nuevo campo de interes del articulo: ")
                self.set_campoInteres(campoInteres)
                print("Campo de Interes modificado correctamente.")
            elif opcion == 9:
                print("Seleccione el estado del Artículo Científico:")
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
                print("Estado modificado correctamente.")
            elif opcion == 10:
                self.asignar_categoria()
            elif opcion == 0:
                band = False
                print("Saliendo de la modificación de el artículo...")
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def eliminar(self):
        print("---Artículo Científico seleccionado---")
        self.consultar()
        
        respuesta = input("¿Está seguro que desea eliminar el artículo? (s/n): ")
        
        if respuesta.lower == "s":
            ArticuloCientifico._instancias.remove(self)
            print("Artículo eliminado correctamente.")
        else:
            print("Eliminación cancelada.")


    def asignar_categoria(self):
        band = True
        if self.__estado == "No Disponible":
            print("No se puede asignar una categoría a un artículo no disponible.")
            return
        if len(Categoria.obtener_instancias()) == 0:
            print("No hay categorías disponibles.")
            return
        while band:
            print("Categorías disponibles:")
            for index in range(len(Categoria.obtener_instancias())):
                print(index + 1, ". ", Categoria.obtener_instancias()[index].get_nombre_categoria())

            opcion = pedir_entero(input("Seleccione una categoría: "))
            opcion -= 1

            if opcion >= 0 and opcion < len(Categoria.obtener_instancias()):
                self.__categoria_articulo = Categoria.obtener_instancias()[opcion]
                print("Categoría asignada correctamente.")
                band = False
            else:
                print("Opción no válida. Intente nuevamente.")