from gestor_biblioteca.share import *

def menu_categoria():
    band = True
    while band:
        clear_console()
        print("--- MENÚ CATEGORÍA ---")
        print("1) Crear categoría")
        print("2) Consultar categoría")
        print("3) Modificar categoría")
        print("4) Eliminar categoría")
        print("0) Salir")

        opcion = pedir_entero("Seleccione una opción: ")
        clear_console()

        if opcion == 1:

            while True:
                print("---- Crear Categoría ----")
                print("1) Crear categoria")
                print("2) Crear subcategoria")
                print("0) Salir")

                opcion = pedir_entero("Seleccione una opción: ")
                if opcion == 1:
                    Categoria.crear(True)
                    break
                elif opcion == 2:
                    Categoria.mostrar_instancias()
                    op= pedir_entero("Seleccione la categoría para crear una subcategoría: ")
                    categoria = Categoria.get_instancia_index(op-1)
                    if categoria is not None:
                        subcategoria = Categoria.crear(False)
                        categoria.agregar_subcategoria(subcategoria)
                        clear_console()
                    break
                elif opcion == 0:
                    print("Saliendo de la creación de categoría...")
                    esperar()
                    break
        elif opcion == 2:
            while True:
                opcion2=pedir_entero("--- Consultar Categoría ---\n\n1) Ver lista de Categorías\n2) Consultar Categoría por ID\n0) Salir\n\nSeleccione una opción: ", True)
                clear_console()

                if opcion2 == 1:
                    print("--- Lista de Tesis registrados ---\n")
                    Categoria.mostrar_categorias()
                    esperar()

                elif opcion2 == 2:
                    print("1) Consultar categoría")
                    print("2) Consultar subcategoría")
                    print("0) Salir")
                    opcion = pedir_entero("Seleccione una opción: ")
                    if opcion == 1:
                        idCategoria = pedir_entero("Ingrese el ID de la categoría a consultar: ")
                        categoria = Categoria.buscar_categoria(idCategoria)
                        if categoria is not None:
                            categoria.consultar()
                            esperar()
                        else:
                            print("Categoría no encontrada.")
                            esperar()
                        break
                
                elif opcion == 2:
                    Categoria.mostrar_instancias()
                    op = pedir_entero("Seleccione la categoría para consultar sus subcategorías: ")
                    categoria = Categoria.get_instancia_index(op-1)
                    if categoria is not None:
                        clear_console()
                        if len(categoria.get_subcategorias()) == 0:
                            print("No hay subcategorías registradas.")
                            esperar()
                        else:
                            print("Subcategorías registradas:")
                            categoria.listar_subcategorias()
                            subcategoria_index = pedir_entero("Seleccione el número de la subcategoría a consultar: ") - 1
                            if 0 <= subcategoria_index < len(categoria.get_subcategorias()):
                                subcategoria = categoria.get_subcategoria_index(subcategoria_index)
                                subcategoria.consultar()
                            else:
                                print("Opción inválida.")
                            esperar()
                    else:
                        print("Categoría no encontrada.")
                        esperar()
                    break
                elif opcion == 0:
                    print("Saliendo de la consulta de categoría...")
                    esperar()
                    break
        elif opcion == 3:
            while True: 
                print ("---- Modificar Categoría ----")
                print ("1) Modificar categoría")
                print ("2) Modificar subcategoría")
                print ("0) Salir")
                op = pedir_entero("Seleccione una opción: ")
                if op == 1:
                    clear_console()
                    idCategoria = pedir_entero("Ingrese el ID de la categoría a modificar: ")
                    categoria = Categoria.buscar_categoria(idCategoria)
                    if categoria is not None:
                        categoria.modificar()
                    else:
                        print("Categoría no encontrada.")
                    esperar()
                    break
                elif op == 2:
                    clear_console()
                    print("Subcategorías registradas:")
                    Categoria.mostrar_instancias()
                    op = pedir_entero("Seleccione la categoría para modificar sus subcategorías: ")
                    categoria = Categoria.get_instancia_index(op-1)
                    if categoria is not None:
                        if len(categoria.get_subcategorias()) == 0:
                            print("No hay subcategorías registradas.")
                        else:
                            print("Subcategorías registradas:")
                            categoria.listar_subcategorias()
                            subcategoria_index = pedir_entero("Seleccione el número de la subcategoría a modificar: ") - 1
                            if 0 <= subcategoria_index < len(categoria.get_subcategorias()):
                                subcategoria = categoria.get_subcategoria_index(subcategoria_index)
                                subcategoria.modificar()
                            else:
                                print("Opción inválida.")
                    else:
                        print("Categoría no encontrada.")
                    esperar()
                    break
                elif op == 0:
                    print("Saliendo de la modificación de categoría...")
                    esperar()
                    break
        elif opcion == 4:
            print("---- Eliminar Categoría ----")
            print("1) Eliminar categoría")
            print("2) Eliminar subcategoría")
            print("0) Salir")
            opcion = pedir_entero("Seleccione una opción: ")
            if opcion == 1:
                idCategoria = pedir_entero("Ingrese el ID de la categoría a eliminar: ")
                categoria = Categoria.buscar_categoria(idCategoria)
                if categoria is not None:
                    categoria.eliminar()
                else:
                    print("Categoría no encontrada.")
                    esperar()
            elif opcion == 2:
                Categoria.mostrar_instancias()
                op = pedir_entero("Seleccione la categoría para eliminar sus subcategorías: ")
                categoria = Categoria.get_instancia_index(op-1)
                if categoria is not None:
                    if len(categoria.get_subcategorias()) == 0:
                        print("No hay subcategorías registradas.")
                    else:
                        print("Subcategorías registradas:")
                        categoria.listar_subcategorias()
                        subcategoria_index = pedir_entero("Seleccione el número de la subcategoría a eliminar: ") - 1
                        if 0 >= subcategoria_index and subcategoria_index < len(categoria.get_subcategorias()):
                            subcategoria = categoria.get_subcategoria_index(subcategoria_index)
                            subcategoria.eliminar()
                        else:
                            print("Opción inválida.")
                            esperar()
                else:
                    print("Categoría no encontrada.")
                    esperar()
        elif opcion == 0:
            band = False
        else:
            print("Opción inválida. Intente nuevamente.")
            esperar()

# -------------------- CLASE CATEGORIA --------------------
class Categoria:
    _instancias=[]
    
    def __init__(self,idCategoria,nombre,descripcion, esPrincipal=True):
        self.__idCategoria=idCategoria
        self.__nombre=nombre
        self.__descripcion=descripcion
        self.__subcategorias = [] # Lista para almacenar subcategorías
        # Solo agregar a _instancias si es una categoría principal
        self.__esPrincipal = esPrincipal
        if esPrincipal: 
            Categoria._instancias.append(self)

    #getters
    def get_idCategoria(self):
        return self.__idCategoria
    def get_nombre(self):
        return self.__nombre
    def get_descripcion(self):
        return self.__descripcion
    def get_subcategorias(self):
        return self.__subcategorias
    def get_esPrincipal(self):
        return self.__esPrincipal
    
    #setters
    def set_idCategoria(self,idCategoria):
        self.__idCategoria=idCategoria
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_descripcion(self,descripcion):
        self.__descripcion=descripcion
    
    # Métodos de instancias
    def buscar_categoria(idCategoria):
        for categoria in Categoria._instancias:
            if categoria.get_idCategoria() == idCategoria:
                return categoria
        return None
    
    def mostrar_categorias():
        if len(Categoria._instancias) == 0:
            print("No hay categorías registradas.")
            esperar()
            return
        print("Categorías registradas:")

        for categoria in Categoria._instancias:     
            if(categoria.get_esPrincipal()):
                print(f" ID: {categoria.get_idCategoria()}, Nombre: {categoria.get_nombre()}, Descripción: {categoria.get_descripcion()}")
            if categoria.get_subcategorias():
                print("   Subcategorías:")
                for subcategoria in categoria.get_subcategorias():
                    print(f"    ID: {subcategoria.get_idCategoria()}, Nombre: {subcategoria.get_nombre()}")
        
    def get_instancia_index(index):
        return Categoria._instancias[index] 
    
    # Métodos para manejar subcategorías
    def agregar_subcategoria(self, subcategoria):
        if isinstance(subcategoria, Categoria): 
            if subcategoria == self:
                print("Error: Una categoría no puede ser subcategoría de sí misma.")
                return
            if subcategoria not in self.__subcategorias:
                self.__subcategorias.append(subcategoria)
                print(f"Subcategoría '{subcategoria.get_nombre()}' agregada a '{self.__nombre}'.")
            else:
                print(f"Error: La subcategoría '{subcategoria.get_nombre()}' ya está asociada a '{self.__nombre}'.")
        else:
            print("Error: La subcategoría debe ser una instancia de la clase Categoria.")
        esperar ()

    def eliminar_subcategoria(self, subcategoria):
        if subcategoria in self.__subcategorias:
            self.__subcategorias.remove(subcategoria)
            print(f"Subcategoría '{subcategoria.get_nombre()}' eliminada de '{self.__nombre}'.")
        else:
            print(f"Error: La subcategoría '{subcategoria.get_nombre()}' no está asociada a '{self.__nombre}'.")

    def listar_subcategorias(self):
        if self.__subcategorias:
            print(f"Subcategorías de '{self.__nombre}':")
            for index, subcategoria in enumerate(self.__subcategorias, start=1):
                print(f"{index}. {subcategoria.get_nombre()}")
        else:
            print(f"La categoría '{self.__nombre}' no tiene subcategorías.")

    def modificar_subcategoria(self):
        if not self.__subcategorias:
            print(f"La categoría '{self.__nombre}' no tiene subcategorías para modificar.")
            return

        # Listar subcategorías
        print(f"Subcategorías de '{self.__nombre}':")
        for index, subcategoria in enumerate(self.__subcategorias, start=1):
            print(f"{index}. {subcategoria.get_nombre()}")

        # Seleccionar subcategoría
        try:
            opcion = pedir_entero("Seleccione el número de la subcategoría a modificar (0 para cancelar): ")
            if opcion == 0:
                print("Modificación de subcategorías cancelada.")
                return

            if 1 <= opcion <= len(self.__subcategorias):
                subcategoria = self.__subcategorias[opcion - 1]
                print(f"Modificando subcategoría '{subcategoria.get_nombre()}':")

                #Que desea modificar
                print("1. ID Subcategoría")
                print("2. Nombre")
                print("3. Descripción")
                opcion_modificacion = pedir_entero("Seleccione la opción a modificar: ")
                if opcion_modificacion == 1:
                    nuevo_id = pedir_entero("Ingrese el nuevo ID: ")
                    while Categoria.buscar_categoria(nuevo_id) != None:
                        print("El id de la subcategoria ya existe.")
                        nuevo_id = pedir_entero("Ingrese el nuevo ID: ")
                    subcategoria.set_idCategoria(nuevo_id)
                elif opcion_modificacion == 2:
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    subcategoria.set_nombre(nuevo_nombre)
                elif opcion_modificacion == 3:
                    nueva_descripcion = input("Ingrese la nueva descripción: ")
                    subcategoria.set_descripcion(nueva_descripcion)
                else:
                    print("Opción inválida. No se realizó ninguna modificación.")
                    return

                print(f"Subcategoría '{nuevo_nombre}' modificada correctamente.")
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    #methods
    def crear(esPrincipal=True):
        idCategoria = pedir_entero("Ingrese el ID de la categoria: ")

        while Categoria.buscar_categoria(idCategoria) is not None:
            print("El ID de la categoria ya existe.")
            idCategoria = pedir_entero("Ingrese el ID de la categoria: ")

        nombre = input("Ingrese el nombre de la categoria: ")
        descripcion = input("Ingrese la descripcion de la categoria: ")

        nueva_categoria = Categoria(idCategoria, nombre, descripcion, esPrincipal)
        print("Categoría creada correctamente." if esPrincipal else "Subcategoría creada correctamente.")
        return nueva_categoria  # Devuelve la instancia creada

    def consultar(self):
        print("ID Categoria: ", self.__idCategoria)
        print("Nombre: ", self.__nombre)
        print("Descripcion: ", self.__descripcion)
        if self.__subcategorias:
            self.listar_subcategorias()


    def modificar(self):
        print("---- Modificar Categoría ----")
        print("1. ID Categoria")
        print("2. Nombre")
        print("3. Descripcion")
        print("4. Subcategorías")
        print("0. Salir")
        opcion=pedir_entero("Seleccione la opción a modificar: ")

        if opcion==1:
            idCategoria=pedir_entero("Ingrese el nuevo id de la categoria: ")

            while Categoria.buscar_categoria(idCategoria) != None:
                print("El id de la categoria ya existe.")
                idCategoria=pedir_entero("Ingrese el nuevo id de la categoria: ")

            self.set_idCategoria(idCategoria)
            print("ID Categoria modificado correctamente.")
        elif opcion==2:
            nombre=input("Ingrese el nuevo nombre de la categoria: ")
            self.set_nombre(nombre)
            print("Nombre modificado correctamente.")
        elif opcion==3:
            descripcion=input("Ingrese la nueva descripcion de la categoria: ")
            self.set_descripcion(descripcion)
            print("Descripcion modificado correctamente.")
        elif opcion==4:
            self.modificar_subcategoria()
        elif opcion==0:
            print("Saliendo de la modificacion de categoria...")
            return
        else:
            print("Opción inválida. No se realizó ninguna modificación.")
            return

    def eliminar(self):
        print("ID Categoria: ", self.__idCategoria)
        print("Nombre: ", self.__nombre)
        print("Descripcion: ", self.__descripcion)
        
        if self.__subcategorias:
            print("Esta categoría tiene subcategorías asociadas:")
            self.listar_subcategorias()
            respuesta = input("¿Desea eliminar también las subcategorías? (s/n): ")
            if respuesta.lower() == "s":
                self.__subcategorias.clear()
                print("Subcategorías eliminadas.")
        
        respuesta = input("¿Está seguro que desea eliminar la categoría? (s/n): ")
        if respuesta.lower() == "s":
            Categoria._instancias.remove(self)
            print("Categoría eliminada correctamente.")
        else:
            print("Categoría no eliminada.")

    def get_subcategoria_index(self, index):
        return self.__subcategorias[index]

    @classmethod
    def obtener_instancias(cls):
        return cls._instancias.deepcopy()  # Retorna una copia de la lista de instancias
    
    #metodos para las instacias
    @classmethod
    def mostrar_instancias(cls):
        if len(cls._instancias) == 0:
            print("No hay categorías registradas.")
            return
        for i, instancia in enumerate(cls._instancias, start=1):
            print(f"{i}. {instancia.get_nombre()}")
            
    
# -------------------- EJEMPLO DE USO SUBCATEGORÍAS --------------------
    
# categoria_principal = Categoria(1, "Ciencia", "Libros de ciencia")
# subcategoria_1 = Categoria(2, "Física", "Libros de física",esPrincipal=False)
# subcategoria_2 = Categoria(3, "Química", "Libros de química",esPrincipal=False)

# # # Agregar subcategorías
# categoria_principal.agregar_subcategoria(subcategoria_1)
# categoria_principal.agregar_subcategoria(subcategoria_2)

# # # Consultar categoría principal
# categoria_principal.consultar()

# # # Eliminar una subcategoría
# categoria_principal.eliminar_subcategoria(subcategoria_1)

# # # Consultar nuevamente
# categoria_principal.consultar()