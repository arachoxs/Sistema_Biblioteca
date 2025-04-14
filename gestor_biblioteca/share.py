def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

