"""
Python program to translate to and from Morse code.

https://en.wikipedia.org/wiki/Morse_code
"""

# fmt: off
MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "@": ".--.-.",
    ":": "---...", ",": "--..--", ".": ".-.-.-", "'": ".----.", '"': ".-..-.",
    "?": "..--..", "/": "-..-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "(": "-.--.", ")": "-.--.-", "!": "-.-.--", " ": "/"
}  # Exclamation mark is not in ITU-R recommendation
# fmt: on
REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def encrypt(message):
    """
    >>> encrypt("Sos!")
    '... --- ... -.-.--'
    >>> encrypt("SOS!") == encrypt("sos!")
    True
    """
    return " ".join(MORSE_CODE_DICT[char] for char in message.upper())

'''
def encrypt(message: str) -> str:
    """
    >>> encrypt("Sos!")
    '... --- ... -.-.--'
    >>> encrypt("SOS!") == encrypt("sos!")
    True
    """
    return " ".join(MORSE_CODE_DICT[char] for char in message.upper())
'''
def decrypt(message):
    """
    >>> decrypt('... --- ... -.-.--')
    'SOS!'
    """
    return "".join(REVERSE_DICT[char] for char in message.split())

'''
def decrypt(message: str) -> str:
    """
    >>> decrypt('... --- ... -.-.--')
    'SOS!'
    """
    return "".join(REVERSE_DICT[char] for char in message.split())
'''

def main() -> None:
    """
    >>> s = "".join(MORSE_CODE_DICT)
    >>> decrypt(encrypt(s)) == s
    True
    """
    print("""1) Encriptar
    2) Desencriptar
    3) Salir""")
    control = True
    while control:
        try:
            options = int(input("Elige una opcion: "))
            if options == 1:
                message = input("Escriba un mensaje: ")
                result = encrypt(message)
                print("Mensaje encriptado: ", result)
            elif options == 2:
                messege = input("Escriba el mensaje a desencriptar: ")
                result = decrypt(message)
                print("Mensaje desencriptado: ", result)
            elif options == 3:
                control = False
                print("Saliendo...")
                exit()
        except ValueError:
            print("Error ingresaste una cadena!!")
    

if __name__ == "__main__":
    main()
