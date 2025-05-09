def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_entero(mensaje, clear_and_wait=False, ignore_empty=False):
    """
    Pide un número entero al usuario y lo devuelve.
    Si el usuario ingresa un valor no válido, se le pide nuevamente.
    Si clear_and_wait es True, limpia la consola y espera a que el usuario presione Enter antes de volver a pedir el número.
    Se recomienda el uso de clear_and_wait para la implementación de menús.
    Si ignore_empty es True, se permite que el usuario ingrese una cadena vacía, en cuyo caso se devuelve None.
    """
    while True:
        try:
            valor = input(mensaje)
            if ignore_empty and valor == "":
                return None
            valor = int(valor)
            return valor
        except ValueError:
            if clear_and_wait:
                clear_console()
                print("Valor no válido. Por favor, ingrese un número entero.")
                esperar()
                clear_console()
            else:
                print("\nValor no válido. Por favor, ingrese un número entero.\n")
                
    
# --- Clase Date ---
# Esta clase representa una fecha y permite operaciones como sumar días y validar fechas.
def esperar():
    input("\nPresione Enter para continuar...")


class Date:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    # Setters
    def set_dia(self, dia):
        """Establece el día de la fecha."""
        self.dia = dia
    def set_mes(self, mes):
        """Establece el mes de la fecha."""
        self.mes = mes
    def set_año(self, año):
        """Establece el año de la fecha."""
        self.año = año
        
    # Getters
    def get_dia(self):
        """Devuelve el día de la fecha."""
        return self.dia
    def get_mes(self):
        """Devuelve el mes de la fecha."""
        return self.mes
    def get_año(self):
        """Devuelve el año de la fecha."""
        return self.año
    
    # --- Métodos de la clase Date ---

    def registrar_fecha():
        """Pide al usuario día, mes y año hasta que ingrese una fecha válida."""
        band = False
        # print("--- Registrando nueva fecha ---\n")
        while(band == False):
            dia = pedir_entero("Ingrese el día: ")
            mes = pedir_entero("Ingrese el mes: ")
            año = pedir_entero("Ingrese el año: ")
            
            fecha=Date(dia,mes,año)

            if fecha.validar_fecha():
                # print(f"\nFecha registrada: {fecha.dia}/{fecha.mes}/{fecha.año}\n")
                band = True
            else:
                print("\nFecha inválida. Intente nuevamente.\n")
        
        return fecha

    def _es_bisiesto(año):
        """Comprueba si un año es bisiesto."""
        return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

    def _dias_en_mes(self):
        """Devuelve el número de días en un mes/año específico."""
        if self.mes < 1 or self.mes > 12:
            return 0 # Mes inválido

        if self.mes == 2:
            return 29 if Date._es_bisiesto(self.año) else 28
        elif self.mes in [4, 6, 9, 11]:
            return 30
        else: # Meses 1, 3, 5, 7, 8, 10, 12
            return 31

    def validar_fecha(self):
        """Valida si los atributos dia, mes, año forman una fecha correcta."""
        if self.mes < 1 or self.mes > 12:
            # print(f"Error: Mes inválido ({self.mes})") # Debug
            return False

        dias_del_mes = self._dias_en_mes()

        if self.dia < 1 or self.dia > dias_del_mes:
            # print(f"Error: Día inválido ({self.dia}) para el mes {self.mes}/{self.año} (max {dias_del_mes} días)") # Debug
            return False

        # No necesitamos validar el año aquí a menos que haya restricciones (ej. año > 0)
        if self.año <= 0 or self.año > 2025:
             # print(f"Error: Año inválido ({self.año})") # Debug
             return False

        return True

    # --- Nuevas funciones ---
    def sumar_dias(self, dias_a_sumar):
        """
        Suma una cantidad de días a la fecha actual.
        Devuelve un *nuevo* objeto date con la fecha resultante.
        No modifica el objeto original.
        Permite sumar días negativos (restar días).
        """
        if dias_a_sumar == 0:
            return Date(self.dia, self.mes, self.año) # Devuelve una copia

        # Crear una copia para no modificar el original
        nueva_fecha = Date(self.dia, self.mes, self.año)

        if dias_a_sumar > 0:
            for _ in range(dias_a_sumar):
                dias_mes_actual = nueva_fecha._dias_en_mes()

                if nueva_fecha.dia < dias_mes_actual:
                    nueva_fecha.dia += 1
                else: # Pasar al siguiente mes
                    nueva_fecha.dia = 1
                    if nueva_fecha.mes < 12:
                        nueva_fecha.mes += 1
                    else: # Pasar al siguiente año
                        nueva_fecha.mes = 1
                        nueva_fecha.año += 1
        else: # Restar días (dias_a_sumar es negativo)
             for _ in range(abs(dias_a_sumar)):
                 if nueva_fecha.dia > 1:
                     nueva_fecha.dia -= 1
                 else: # Retroceder al mes anterior
                     if nueva_fecha.mes > 1:
                         nueva_fecha.mes -= 1
                     else: # Retroceder al año anterior
                         nueva_fecha.mes = 12
                         nueva_fecha.año -= 1
                         # Validar año 0 o negativo si se resta mucho
                         if nueva_fecha.año <= 0:
                              raise ValueError("La resta de días resulta en un año inválido (<= 0).")

                     # El día pasa a ser el último día del nuevo mes/año
                     nueva_fecha.dia = self._dias_en_mes(nueva_fecha.mes, nueva_fecha.año)

        return nueva_fecha

    # --- Métodos de comparación útiles para diferencia_fechas ---
    def __eq__(self, other):
        
        """Comprueba si dos fechas son iguales."""
        if not isinstance(other, Date):
            return NotImplemented # No comparar con tipos diferentes
        return self.año == other.año and self.mes == other.mes and self.dia == other.dia

    def __lt__(self, other):
        """Comprueba si esta fecha es anterior a otra."""
        if not isinstance(other, Date):
            return NotImplemented
        if self.año < other.año:
            return True
        if self.año == other.año:
            if self.mes < other.mes:
                return True
            if self.mes == other.mes:
                return self.dia < other.dia
        return False

    def __le__(self, other):
        """Comprueba si esta fecha es anterior o igual a otra."""
        return self < other or self == other

    def __gt__(self, other):
        """Comprueba si esta fecha es posterior a otra."""
        return not (self <= other)

    def __ge__(self, other):
        """Comprueba si esta fecha es posterior o igual a otra."""
        return not (self < other)

    # --- Método para representar la fecha como string ---
    def __str__(self):
        """Representación legible de la fecha."""
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}" # Formato DD/MM/AAAA

    def __repr__(self):
        """Representación para debuggeo."""
        return f"date({self.dia}, {self.mes}, {self.año})"


# --- Nueva función externa ---

def diferencia_fechas(fecha1, fecha2):
    """
    Calcula la diferencia en días entre dos objetos date.
    Devuelve un entero que representa el número de días entre las fechas.
    Si fecha1 es posterior a fecha2, el resultado será positivo.
    Si fecha1 es anterior a fecha2, el resultado será negativo.
    Si las fechas son iguales, el resultado será cero.
    """
    # Determinar el orden de las fechas
    if fecha1 == fecha2:
        return 0

    # Copiamos las fechas para no modificarlas
    fecha_temp = Date(fecha1.dia, fecha1.mes, fecha1.año)
    fecha_objetivo = Date(fecha2.dia, fecha2.mes, fecha2.año)
    contador_dias = 0

    # Determinar la dirección del conteo
    incremento = 1 if fecha1 < fecha2 else -1

    # Iteramos día por día en la dirección adecuada
    while fecha_temp != fecha_objetivo:
        if incremento > 0:  # Avanzar un día
            dias_mes_actual = fecha_temp._dias_en_mes()
            if fecha_temp.dia < dias_mes_actual:
                fecha_temp.dia += 1
            else:  # Pasar al siguiente mes
                fecha_temp.dia = 1
                if fecha_temp.mes < 12:
                    fecha_temp.mes += 1
                else:  # Pasar al siguiente año
                    fecha_temp.mes = 1
                    fecha_temp.año += 1
        else:  # Retroceder un día
            if fecha_temp.dia > 1:
                fecha_temp.dia -= 1
            else:  # Retroceder al mes anterior
                if fecha_temp.mes > 1:
                    fecha_temp.mes -= 1
                else:  # Retroceder al año anterior
                    fecha_temp.mes = 12
                    fecha_temp.año -= 1
                fecha_temp.dia = fecha_temp._dias_en_mes()

        contador_dias += incremento

        # Medida de seguridad para evitar bucles infinitos si algo falla
        if abs(contador_dias) > 365 * 300:  # Límite arbitrario (aprox 300 años)
            raise OverflowError("La diferencia de fechas es demasiado grande o hay un bucle infinito.")

    return contador_dias
