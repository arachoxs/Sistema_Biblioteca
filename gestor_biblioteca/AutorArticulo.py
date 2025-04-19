from gestor_biblioteca.share import *
from gestor_biblioteca.Autor import Autor

class AutorArticulo:
    _instancias = []

    def __init__(self, articulo, autor):
        self.__autor = autor
        self.__articulo = articulo

        AutorArticulo._instancias.append(self)

    # getters
    def get_autor(self):
        return self.__autor

    def get_articulo(self):
        return self.__articulo
    
    # setters
    def set_autor(self, autor):
        self.__autor = autor
    
    def set_articulo(self, articulo):
        self.__articulo = articulo

    def relacionar_autor_articulo(articulo):
        from gestor_biblioteca.ArticuloCientifico import ArticuloCientifico

        while True:
            print("\n--- Autores disponibles ---")
            print("0. Agregar nuevo autor")
            Autor.mostrar_autores()
            opcion = pedir_entero("Seleccione una opción: ") - 1

            # Registrar nuevo autor
            if opcion == -1:
                Autor.registrar()
                autor_sel = Autor._instancias[-1]
            
            elif 0 <= opcion < len(Autor._instancias):
                autor_sel = Autor.get_instancia_index(opcion)

            else:
                print("Opción no válida, intente nuevamente.")
                continue
                
            #crear la relación autor-articulo
            AutorArticulo(articulo, autor_sel)
            print(f"Autor «{autor_sel.get_nombre()}» relacionado correctamente con «{articulo.get_titulo()}».")
            esperar()

            while True:
                print("\n¿Desea relacionar otro autor?")
                print("1. Sí")
                print("2. No")
                continuar = pedir_entero("Seleccione una opción: ")

                if continuar == 1:
                    break
                elif continuar == 2:
                    print("Saliendo de la relacion de autores...")
                    esperar()
                    return
                else:
                    print("Opción no válida, intente nuevamente.")

    
    def buscar_articulos(autor):
        articulos = []
        for autor_articulo in AutorArticulo._instancias:
            if autor_articulo.get_autor() == autor:
                print(autor_articulo.get_articulo().get_titulo())

        if len(articulos) == 0:
            print("El autor no tiene articulos relacionados.")
        else:
            print("Articulos registrados para este autor:")
            for articulo in articulos:
                print(articulo.get_titulo())
            
        esperar()

    def buscar_autores(articulo):
        autores = []
        for autor_articulo in AutorArticulo._instancias:
            if autor_articulo.get_articulo() == articulo:
                print(autor_articulo.get_autor().get_nombre())

        if len(autores) == 0:
            print("El articulo no tiene autores relacionados.")
        else:
            print("Autores registrados para este articulo:")
            for autor in autores:
                print(autor.get_nombre())
                
        esperar()