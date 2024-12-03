#Nombre en japones

japanesse_names = {"A": "KA",
                   "B": "TU",
                   "C": "MI",
                   "D": "TE",
                   "E": "KU",
                   "F": "LU",
                   "G": "JI",
                   "H": "RI",
                   "I": "KI",
                   "J": "ZU",
                   "K": "ME",
                   "L": "TA",
                   "M": "RIN",
                   "N": "TO",
                   "O": "MO",
                   "P": "NO",
                   "Q": "KE",
                   "R": "SHI",
                   "S": "ARI",
                   "T": "CHI",
                   "U": "DO",
                   "V": "RU",
                   "W": "MEI",
                   "X": "NA",
                   "Y": "FU",
                   "Z": "RA"
                   }

reverse_dict = {value: key for value, key in japanesse_names.items()}

def spanish_to_japanesse(text):
    return " ".join(japanesse_names[char] for char in text.upper())

def japanesse_to_spanish(text):
    return " ".join(reverse_dict[char] for char in text.split())

def main() -> None:
    """
    >>> s = "".join(MORSE_CODE_DICT)
    >>> decrypt(encrypt(s)) == s
    True
    """
    print("""1) Español-Japones
2) Japones-Español
3) Salir""")
    control = True
    while control:
        try:
            options = int(input("Elige una opcion: "))
            if options == 1:
                message = input("Escriba un mensaje: ")
                result = spanish_to_japanesse(message)
                print("Mensaje encriptado: ", result)
            elif options == 2:
                messege = input("Escriba el mensaje a desencriptar: ")
                result = japanesse_to_spanish(message)
                print("Mensaje desencriptado: ", result)
            elif options == 3:
                control = False
                print("Saliendo...")
                exit()
        except ValueError:
            print("Error ingresaste una cadena!!")
    

if __name__ == "__main__":
    main()

    
