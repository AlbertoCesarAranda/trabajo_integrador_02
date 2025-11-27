import secrets
import string

diccionario = {
    'letras': string.ascii_letters,
    'numeros': string.digits,
    'caracteres': string.punctuation
}

while True:
    print("\nGENERADOR DE CONTRASEÑAS")
    print("1. Solo Letras")
    print("2. Solo Números")
    print("3. Letras y Números")
    print("4. Letras, Números y Caracteres")
    print("0. Salir")

    opcion = input("Elija una opción: ").strip()

    if opcion == "0":
        print("Saliendo del programa...")
        print("Gracias por utilizar nuestros sistemas.")
        break

    
    if opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida.")
        continue

    longitud = input("Ingrese la longitud de la contraseña (mínimo 6): ").strip()

    if not longitud.isdigit():
        print("Debe ingresar un número.")
        continue

    longitud = int(longitud)

    if longitud < 6:
        print("La longitud mínima es 6.")
        continue

    
    if opcion == "1":
        tipo = diccionario['letras']
    elif opcion == "2":
        tipo = diccionario['numeros']
    elif opcion == "3":
        tipo = diccionario['letras'] + diccionario['numeros']
    elif opcion == "4":
        tipo = diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']

    
    password = ''.join(secrets.choice(tipo) for _ in range(longitud))

    print("\nContraseña generada:", password)
