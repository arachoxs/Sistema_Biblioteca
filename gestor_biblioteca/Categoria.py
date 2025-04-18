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
            self.__subcategorias.append(subcategoria)
            print(f"Subcategoría '{subcategoria.get_nombre()}' agregada a '{self.__nombre}'.")
        else:
            print("Error: La subcategoría debe ser una instancia de la clase Categoria.")

    def eliminar_subcategoria(self, subcategoria):
        if subcategoria in self.__subcategorias:
            self.__subcategorias.remove(subcategoria)
            print(f"Subcategoría '{subcategoria.get_nombre()}' eliminada de '{self.__nombre}'.")
        else:
            print("Error: La subcategoría no está asociada a esta categoría.")

    def listar_subcategorias(self):
        if self.__subcategorias:
            print(f"Subcategorías de '{self.__nombre}':")
            for subcategoria in self.__subcategorias:
                print(f"- {subcategoria.get_nombre()}")
        else:
            print(f"La categoría '{self.__nombre}' no tiene subcategorías.")

    #methods
    def crear():
        idCategoria=pedir_entero(input("Ingrese el id de la categoria: "))
        nombre=input("Ingrese el nombre de la categoria: ")
        descripcion=input("Ingrese la descripcion de la categoria: ")
    
        Categoria(idCategoria,nombre,descripcion)

    def consultar(self):
        print("ID Categoria: ", self.__idCategoria)
        print("Nombre: ", self.__nombre)
        print("Descripcion: ", self.__descripcion)

    def modificar(self):
        print("ID Categoria: ", self.__idCategoria)
        print("Nombre: ", self.__nombre)
        print("Descripcion: ", self.__descripcion)
        
        idCategoria=pedir_entero(input("Ingrese el nuevo id de la categoria: "))
        nombre=input("Ingrese el nuevo nombre de la categoria: ")
        descripcion=input("Ingrese la nueva descripcion de la categoria: ")
        
        self.set_idCategoria(idCategoria)
        self.set_nombre(nombre)
        self.set_descripcion(descripcion)

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
        return cls._instancias.copy()
    
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
