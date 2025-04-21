from gestor_biblioteca.share import pedir_entero, clear_console, esperar
from gestor_biblioteca.Categoria import Categoria
from gestor_biblioteca.Autor import Autor
from gestor_biblioteca.AutorLibro import AutorLibro

def menu_libro():
    """Menú principal para gestionar libros."""
    while True:
        clear_console()
        opcion = pedir_entero("--- Menú Libro ---\n\n1) Registrar libro\n2) Consultar libro\n3) Modificar libro\n4) Inhabilitar libro\n0) Salir\n\nSeleccione una opción: ", True)
        clear_console()
        if opcion == 1:
            print("--- Registrar libro ---")
            Libro.registrar()

        elif opcion == 2:
            print("--- Consultar libro ---")
            isbn = input("Ingrese el ISBN del libro a consultar: ").strip()
            libro = Libro.buscar_libro(isbn)
            if libro:
                libro.consultar()
            else:
                print("El libro no existe.")
                esperar()

        elif opcion == 3:
            print("--- Modificar libro ---")
            isbn = input("Ingrese el ISBN del libro a modificar: ").strip()
            libro = Libro.buscar_libro(isbn)
            if libro:
                libro.modificar()
            else:
                print("El libro no existe.")
                esperar()

        elif opcion == 4:
            print("--- Inhabilitar libro ---")
            isbn = input("Ingrese el ISBN del libro a inhabilitar: ").strip()
            libro = Libro.buscar_libro(isbn)
            if libro:
                libro.inhabilitar()
                print("Libro inhabilitado correctamente.")
                esperar()
            else:
                print("El libro no existe.")
                esperar()

        elif opcion == 0:
            print("Saliendo del menú de libros...")
            esperar()
            break

        else:
            print("Opción no válida, intente nuevamente.")
            esperar()


class Libro:
    _instancias = []

    def __init__(self, isbn, titulo, edicion, año, editorial, genero, idioma, n_copias, activo=True):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__edicion = edicion
        self.__año = año
        self.__editorial = editorial
        self.__genero = genero
        self.__idioma = idioma
        self.__n_copias = n_copias
        self.__activo = activo
        self.__categoria_libro = None

        Libro._instancias.append(self)

    # Getters
    def get_isbn(self):
        return self.__isbn

    def get_titulo(self):
        return self.__titulo

    def get_edicion(self):
        return self.__edicion

    def get_año(self):
        return self.__año

    def get_editorial(self):
        return self.__editorial

    def get_genero(self):
        return self.__genero

    def get_idioma(self):
        return self.__idioma

    def get_n_copias(self):
        return self.__n_copias

    def get_activo(self):
        return self.__activo

    # Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_edicion(self, edicion):
        self.__edicion = edicion

    def set_año(self, año):
        self.__año = año

    def set_editorial(self, editorial):
        self.__editorial = editorial

    def set_genero(self, genero):
        self.__genero = genero

    def set_n_copias(self, n_copias):
        self.__n_copias=n_copias

    def set_idioma(self, idioma):
        self.__idioma = idioma

    def set_activo(self, activo):
        self.__activo = activo

    # Métodos de clase
    @staticmethod
    def buscar_libro(isbn):
        """Busca un libro por su ISBN."""
        for libro in Libro._instancias:
            if libro.get_isbn() == isbn:
                return libro
        return None

    @staticmethod
    def registrar():
        """Registra un nuevo libro."""
        from gestor_biblioteca.Copia import Copia  # Importación dentro del método

        isbn = input("Ingrese el ISBN del libro: ").strip()

        # Verificar unicidad del ISBN
        while Libro.buscar_libro(isbn):
            print("El ISBN ya existe, pruebe con otro valor.")
            isbn = input("Ingrese el ISBN del libro: ").strip()

        titulo = input("Ingrese el título del libro: ").strip()
        edicion = pedir_entero("Ingrese la edición del libro: ")
        año = pedir_entero("Ingrese el año del libro: ")
        editorial = input("Ingrese la editorial del libro: ").strip()
        genero = input("Ingrese el género del libro: ").strip()
        idioma = input("Ingrese el idioma del libro: ").strip()
        n_copias = pedir_entero("Ingrese el número de copias del libro: ")

        # Validar que el número de copias sea mayor o igual a 1
        while n_copias < 1:
            print("El número de copias debe ser mayor o igual a 1.")
            n_copias = pedir_entero("Ingrese el número de copias del libro: ")

        # Crear el libro
        libro = Libro(isbn, titulo, edicion, año, editorial, genero, idioma, n_copias)
        libro.asignar_categoria()  # Asignar categoría al libro
        AutorLibro.relacionar_autor_libro(libro)  # Relacionar autor al libro

        # Crear copias del libro
        Copia.generar_copias(n_copias, libro)

        print("Libro registrado correctamente.")
        esperar()

    def consultar(self):
        """Muestra la información del libro."""
        print(f"ISBN: {self.__isbn}")
        print(f"Título: {self.__titulo}")
        print(f"Edición: {self.__edicion}")
        print(f"Año: {self.__año}")
        print(f"Editorial: {self.__editorial}")
        print(f"Género: {self.__genero}")
        print(f"Idioma: {self.__idioma}")
        print(f"Número de copias: {self.__n_copias}")
        print(f"Estado: {'Activo' if self.__activo else 'Inactivo'}")
        print(f"Categoría: {self.__categoria_libro.get_nombre() if self.__categoria_libro else 'No asignada'}")
        print("-- Autores del libro --")
        AutorLibro.buscar_autores(self)
        esperar()

    def modificar(self):
        """Permite modificar los datos del libro."""
        if not self.__activo:
            print("El libro no se encuentra activo, no se puede modificar.")
            esperar()
            return

        while True:
            print("\n--- Modificar Libro ---")
            print("1. Título")
            print("2. Edición")
            print("3. Año")
            print("4. Editorial")
            print("5. Género")
            print("6. Idioma")
            print("7. Asignar nueva categoría")
            print("8. Relacionar nuevo autor")
            print("0. Salir")

            opcion = pedir_entero("Seleccione una opción: ")

            if opcion == 1:
                self.set_titulo(input("Ingrese el nuevo título del libro: ").strip())
            elif opcion == 2:
                self.set_edicion(pedir_entero("Ingrese la nueva edición del libro: "))
            elif opcion == 3:
                self.set_año(pedir_entero("Ingrese el nuevo año del libro: "))
            elif opcion == 4:
                self.set_editorial(input("Ingrese la nueva editorial del libro: ").strip())
            elif opcion == 5:
                self.set_genero(input("Ingrese el nuevo género del libro: ").strip())
            elif opcion == 6:
                self.set_idioma(input("Ingrese el nuevo idioma del libro: ").strip())
            elif opcion == 7:
                self.asignar_categoria()
            elif opcion == 8:
                AutorLibro.relacionar_autor_libro(self)
                print("Autor relacionado correctamente.")
                esperar()
            elif opcion == 0:
                print("Saliendo de la modificación del libro...")
                esperar()
                break
            else:
                print("Opción no válida, intente nuevamente.")

    def inhabilitar(self):
        """Inhabilita el libro."""
        self.__activo = False
        print("El libro ha sido inhabilitado.")

    def asignar_categoria(self):
        """Asigna una categoría al libro."""
        if not self.__activo:
            print("El libro no se encuentra activo, no se puede asignar categoría.")
            esperar()
            return

        if not Categoria._instancias:
            print("No hay categorías disponibles para asignar.")
            esperar()
            return

        while True:
            print("Categorías disponibles:")
            Categoria.mostrar_instancias()
            print("0. Salir")

            opcion = pedir_entero("Seleccione una categoría: ") - 1

            if 0 <= opcion < len(Categoria._instancias):
                self.__categoria_libro = Categoria.get_instancia_index(opcion)
                print("Categoría asignada correctamente.")
                esperar()
                break
            elif opcion == -1:
                print("Saliendo de la asignación de categoría...")
                esperar()
                break
            else:
                print("Opción no válida, intente nuevamente.")

