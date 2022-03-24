import random


def adivina_el_numero(x):

    print("=====================")
    print("Bienvenido al juego!")
    print("=====================")
    print("tu meta es adivinar el número generado por la computadora")


    número_aleatorio = random.randint(1, x) #Numero aleatorio entre 1 y x.

    predicción = 0 #variable

    while predicción != número_aleatorio:   #while = siclo while = porque necesitamos repetir una secuencia de funciones.

        #el usuario ingresa un numero...
        predicción = int(input(f"Adivinia un número entre 1  y {x}: ")) #f-string (tipo de string)

        if predicción < número_aleatorio:
            print('Intenta otra vez, este número es muy pequeño.')
        elif predicción > número_aleatorio:
            print('Este número es muy grande.')

    print(f'Felicitaciones!!! Adivinaste el numero {número_aleatorio} correcto. Ganaste')


adivina_el_numero(10)


