#Busqueda lineal 2.0
import pyttsx3
import speech_recognition as sr


def create_list():
    arr = []
    numElementos = int(input("Cuantos elementos deseas agregar?: "))
    for _ in range(numElementos):
        element = int(input("Elemento a agregar: "))
        arr.append(element)

    return arr


def main_menu():
    print(""" 1) Busqueda lineal
              2) Busqueda binaria
              3) Salir""")


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen(audio):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Elige una opcion")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="es-ES")
        print("Texto reconocido:", text)
        return text
    except sr.UnknownValueError:
        print("No se pudo reconocer el texto")
    except sr.RequestError as e:
        print("Error al solicitar el reconocimiento de voz:", e)
    return None


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print(f"El elemento {x} fue encontrado en el indice: {i}")
            return i

    print(f"El elemento {x} no fue encontrado!")
    return -1


def binary_search(arr, x):

    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
         # Comprueba si x está en el medio
        if arr[mid] == x:
            return mid
         # Si x es mayor, ignora la mitad izquierda
        elif arr[mid] < x:
            left = mid + 1
         # Si x es menor, ignora la mitad derecha
        else:
            right = mid - 1

    return -1

if __name__ == '__main__':
    while True:
        main_menu()
        option = int(input("Por favor elija una opcion: "))
        if option == 3:
            break

        say(f"Elegiste la opcion {option}")

        if option == 1:
            lst = create_list()
            x = int(input("¿Qué elemento deseas buscar?: "))
            index = linear_search(lst, x)
            say(f"El elemento {x} fue encontrado en el indice {index}" if index != -1 else f"El elemento {x} no fue encontrado")
        elif option == 2:
            lst = create_list()
            lst.sort()  # La lista debe estar ordenada para la búsqueda binaria
            x = int(input("¿Qué elemento deseas buscar?: "))
            index = binary_search(lst, x)
            say(f"El elemento {x} fue encontrado en el indice {index}" if index != -1 else f"El elemento {x} no fue encontrado")
        else:
            print("Opción no válida. Por favor, elija una opción válida.")
        
    


    
