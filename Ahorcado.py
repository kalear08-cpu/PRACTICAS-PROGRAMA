import random


PALABRAS = (
    "python", "programacion", "computadora", "teclado", "aventura",
    "mariposa", "biblioteca", "elefante", "montaña", "chocolate",
)
MAX_ERRORES = 6


def mostrar_estado(palabra, letras):
    return " ".join(letra if letra in letras else "_" for letra in palabra)


def jugar():
    palabra = random.choice(PALABRAS).lower()
    acertadas = set()
    usadas = set()
    errores = 0

    print("\n=== AHORCADO ===")
    print(f"Tienes {MAX_ERRORES} intentos incorrectos.")

    while errores < MAX_ERRORES:
        print(f"\nPalabra: {mostrar_estado(palabra, acertadas)}")
        print("Letras usadas:", " ".join(sorted(usadas)) or "ninguna")
        letra = input("Escribe una letra: ").strip().lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Introduce una sola letra.")
            continue
        if letra in usadas:
            print("Ya has usado esa letra.")
            continue

        usadas.add(letra)
        if letra in palabra:
            acertadas.add(letra)
            print("¡Correcto!")
            if all(letra in acertadas for letra in palabra):
                print(f"¡Ganaste! La palabra era: {palabra}")
                return
        else:
            errores += 1
            print(f"Incorrecto. Te quedan {MAX_ERRORES - errores} intentos.")

    print(f"Perdiste. La palabra era: {palabra}")


if __name__ == "__main__":
    jugar()