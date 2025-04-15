def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

class date:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
        
    def registrar_fecha(self):
        band = False
        
        while(band == False):
            self.dia = pedir_entero("Ingrese el dia: ")
            self.mes = pedir_entero("Ingrese el mes: ")
            self.año = pedir_entero("Ingrese el año: ")
            
            if self.validar_fecha():
                band = True
            else:
                print("Fecha inválida. Intente nuevamente.")
        
    def validar_fecha(self):
        if self.mes < 1 or self.mes > 12:
            return False
        
        if self.dia < 1 or self.dia > 31:
            return False
        
        if self.mes == 2:
            if (self.año % 4 == 0 and self.año % 100 != 0) or (self.año % 400 == 0):
                if self.dia > 29:
                    return False
            else:
                if self.dia > 28:
                    return False
        
        if (self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11) and self.dia > 30:
            return False
        
        return True

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"