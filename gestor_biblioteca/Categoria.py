from gestor_biblioteca.share import pedir_entero

class Categoria:
    _instancias=[]
    
    def __init__(self,idCategoria,nombre,descripcion):
        self.__idCategoria=idCategoria
        self.__nombre=nombre
        self.__descripcion=descripcion
        self.__subcategorias = [] # Lista para almacenar subcategorías
        Categoria._instancias.append(self)

    #getters
    def get_idCategoria(self):
        return self.__idCategoria
    def get_nombre(self):
        return self.__nombre
    def get_descripcion(self):
        return self.__descripcion
    def get_subcategorias(self):
        return self.__subcategorias.copy()  # Retorna una copia de la lista de subcategorías
    
    #setters
    def set_idCategoria(self,idCategoria):
        self.__idCategoria=idCategoria
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_descripcion(self,descripcion):
        self.__descripcion=descripcion
    
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

    #methods
    def crear():
        idCategoria=pedir_entero(input("Ingrese el id de la categoria: "))

        while Categoria.buscar_categoria(idCategoria) != None:
            print("El id de la categoria ya existe.")
            idCategoria=pedir_entero("Ingrese el id de la categoria: ")

        nombre=input("Ingrese el nombre de la categoria: ")
        descripcion=input("Ingrese la descripcion de la categoria: ")
    
        Categoria(idCategoria,nombre,descripcion)

    def consultar(self):
        print("ID Categoria: ", self.__idCategoria)
        print("Nombre: ", self.__nombre)
        print("Descripcion: ", self.__descripcion)
        print("Subcategorías:")
        if self.__subcategorias:
            self.listar_subcategorias()


    def modificar(self):
        print("ID Categoria: ", self.__idCategoria)
        print("Nombre: ", self.__nombre)
        print("Descripcion: ", self.__descripcion)
        
        # Modificar atributos de la categoría principal
        idCategoria = pedir_entero(input("Ingrese el nuevo id de la categoria: "))
        nombre = input("Ingrese el nuevo nombre de la categoria: ")
        descripcion = input("Ingrese la nueva descripcion de la categoria: ")
        
        self.set_idCategoria(idCategoria)
        self.set_nombre(nombre)
        self.set_descripcion(descripcion)
        
        # Modificar subcategorías
        while True:
            print("\nOpciones para subcategorías:")
            print("1. Listar subcategorías")
            print("2. Modificar una subcategoría")
            print("3. Agregar una nueva subcategoría")
            print("4. Eliminar una subcategoría")
            print("5. Salir")
            
            opcion = pedir_entero(input("Seleccione una opción: "))
            
            if opcion == 1:
                self.listar_subcategorias()
            elif opcion == 2:
                if not self.__subcategorias:
                    print("No hay subcategorías para modificar.")
                    continue
                self.listar_subcategorias()
                index = pedir_entero("Seleccione el número de la subcategoría a modificar: ") - 1
                if 0 <= index < len(self.__subcategorias):
                    subcategoria = self.__subcategorias[index]
                    print(f"Modificando subcategoría '{subcategoria.get_nombre()}':")
                    subcategoria.modificar()
                else:
                    print("Opción inválida.")
            elif opcion == 3:
                idSubcategoria = pedir_entero("Ingrese el id de la nueva subcategoría: ")
                nombreSubcategoria = input("Ingrese el nombre de la nueva subcategoría: ")
                descripcionSubcategoria = input("Ingrese la descripción de la nueva subcategoría: ")
                nueva_subcategoria = Categoria(idSubcategoria, nombreSubcategoria, descripcionSubcategoria)
                self.agregar_subcategoria(nueva_subcategoria)
            elif opcion == 4:
                if not self.__subcategorias:
                    print("No hay subcategorías para eliminar.")
                    continue
                self.listar_subcategorias()
                index = pedir_entero(input("Seleccione el número de la subcategoría a eliminar: ")) - 1
                if 0 <= index < len(self.__subcategorias):
                    subcategoria = self.__subcategorias[index]
                    self.eliminar_subcategoria(subcategoria)
                else:
                    print("Opción inválida.")
            elif opcion == 5:
                print("Saliendo de la modificación de subcategorías.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def eliminar(self):
        print("ID Categoria: ", self.__idCategoria)
        print("Nombre: ", self.__nombre)
        print("Descripcion: ", self.__descripcion)
        
        respuesta = input("¿Está seguro que desea eliminar la categoría? (s/n): ")
        
        if respuesta.lower() == "s":
            Categoria._instancias.remove(self)
            print("Categoría eliminada")
        else:
            print("Categoría no eliminada")

    @classmethod
    def obtener_instancias(cls):
        return cls._instancias.deepcopy()  # Retorna una copia de la lista de instancias
    
    #metodos para las instacias
    def mostrar_instancias(cls):
        if len(cls._instancias) == 0:
            print("No hay categorias registradas")
            return 
        else:
            for i in range(len(cls._instancias)):
                print(i+1,". ",cls._instancias[i].get_nombre())
            
    def get_instancia_index(cls,index):
        return cls._instancias[index]
    
# -------------------- EJEMPLO DE USO SUBCATEGORÍAS --------------------
    
# categoria_principal = Categoria(1, "Ciencia", "Libros de ciencia")
# subcategoria_1 = Categoria(2, "Física", "Libros de física")
# subcategoria_2 = Categoria(3, "Química", "Libros de química")

# Agregar subcategorías
# categoria_principal.agregar_subcategoria(subcategoria_1)
# categoria_principal.agregar_subcategoria(subcategoria_2)

# Consultar categoría principal
# categoria_principal.consultar()

# Eliminar una subcategoría
#categoria_principal.eliminar_subcategoria(subcategoria_1)

# Consultar nuevamente
# categoria_principal.consultar()
