from gestor_biblioteca.share import *
from gestor_biblioteca.Autor import Autor

class AutorTesis:
    _instancias = []

    def __init__(self, tesis, autor):
        self.__autor = autor
        self.__tesis = tesis

        AutorTesis._instancias.append(self)

    # getters
    def get_autor(self):
        return self.__autor

    def get_tesis(self):
        return self.__tesis
    
    # setters
    def set_autor(self, autor):
        self.__autor = autor
    
    def set_tesis(self, tesis):
        self.__tesis = tesis
    

    def relacionar_autor_tesis(tesis):
        from gestor_biblioteca.Tesis import Tesis

        while True:
            print("\n--- Autores disponibles ---")
            print("0. Agregar nuevo autor")
            Autor.mostrar_autores() # Mostrar autores existentes
            opcion = pedir_entero("Seleccione una opción: ") - 1

            # Registrar nuevo autor
            if opcion == -1:
                Autor.registrar() # Agregar nuevo autor
                autor_sel = Autor._instancias[-1] # Seleccionar el último autor agregado

            # Seleccionar autor existente
            elif 0 <= opcion < len(Autor._instancias):
                autor_sel = Autor.get_instancia_index(opcion) # Obtener el autor seleccionado
                
            else:
                print("Opción no válida, intente nuevamente.")
                continue

            # Crear la relación autor–libro
            AutorTesis(tesis,autor_sel)
            print(f"Autor «{autor_sel.get_nombre()}» relacionado correctamente con «{tesis.get_nombre()}».")
            
            while True:
                print("\n¿Desea relacionar otro autor?")
                print("1. Sí")
                print("2. No")
                continuar = pedir_entero("Seleccione una opción: ")

                if continuar == 1:
                    break  # Vuelve al inicio del bucle principal
                elif continuar == 2:
                    print("Saliendo de la relación de autores...")
                    return
                else:
                    print("Opción no válida, intente nuevamente.")          

    def buscar_tesis(autor):
        tesis=[]
        for autor_tesis in AutorTesis._instancias:
            if autor_tesis.get_autor() == autor:
                print (autor_tesis.get_tesis().get_nombre())

        if len(tesis)==0:
            print("No se encontraron tesis relacionadas con el autor seleccionado.")
        else:
            print("Tesis relacionadas con el autor seleccionado:")
            for tesis in tesis:
                print(tesis.get_nombre())

    def buscar_autores(tesis):
        autores=[]
        for autor_tesis in AutorTesis._instancias:
            if autor_tesis.get_tesis() == tesis:
                print (autor_tesis.get_autor().get_nombre())

        if len(autores)==0:
            print("No se encontraron autores relacionados con la tesis seleccionada.")
        else:
            print("Autores relacionados con la tesis seleccionada:")
            for autor in autores:
                print(autor.get_nombre())