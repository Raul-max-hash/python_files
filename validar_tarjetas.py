"""
Funciones para verificar la validez de los números de tarjetas de crédito.

https://en.wikipedia.org/wiki/Luhn_algorithm
"""


def validate_initial_digits(credit_card_number: str) -> bool:
    """
    Función para validar los dígitos iniciales de un número de tarjeta de crédito dado.
    """
    return credit_card_number.startswith(("34", "35", "37", "4", "5", "6"))


def luhn_validation(credit_card_number: str) -> bool:
    """
    Función para validar un número de tarjeta de crédito usando el algoritmo de Luhn.
    """
    cc_number = credit_card_number
    total = 0
    half_len = len(cc_number) - 2
    for i in range(half_len, -1, -2):
        # Duplicar el valor de cada segundo dígito
        digit = int(cc_number[i])
        digit *= 2
        # Si la duplicación de un número resulta en un número de dos dígitos
        # (por ejemplo, 6 x 2 = 12), entonces suma los dígitos del producto
        # para obtener un número de un solo dígito.
        if digit > 9:
            digit %= 10
            digit += 1
        cc_number = cc_number[:i] + str(digit) + cc_number[i + 1 :]
        total += digit

    # Sumar los dígitos restantes
    for i in range(len(cc_number) - 1, -1, -2):
        total += int(cc_number[i])

    return total % 10 == 0


def validate_credit_card_number(credit_card_number: str) -> bool:
    """
    Función para validar un número de tarjeta de crédito dado.
    """
    error_message = f"{credit_card_number} es un número de tarjeta de crédito inválido porque"
    if not credit_card_number.isdigit():
        print(f"{error_message} tiene caracteres no numéricos.")
        return False

    if not 13 <= len(credit_card_number) <= 16:
        print(f"{error_message} su longitud es incorrecta.")
        return False

    if not validate_initial_digits(credit_card_number):
        print(f"{error_message} sus dos primeros dígitos son incorrectos.")
        return False

    if not luhn_validation(credit_card_number):
        print(f"{error_message} no pasa la verificación de Luhn.")
        return False

    print(f"{credit_card_number} es un número de tarjeta de crédito válido.")
    return True


def main():
    while True:
        print("\nOpciones del Menú:")
        print("1. Validar un número de tarjeta de crédito")
        print("2. Salir")
        opcion = input("Elige una opción (1/2): ")

        if opcion == "1":
            cc_number = input("Introduce el número de tarjeta de crédito: ")
            validate_credit_card_number(cc_number)
        elif opcion == "2":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")


if __name__ == "__main__":
    main()
