import random


def adivina_el_número_computadora(x):  #Función
    print('-------------------------')
    print('Bienvenido!!!')
    print('-------------------------')
    print(f'Selecciona un numero entre 1 y {x} para que la computadora intente adivinar...')


    límite_inferior = 1
    límite_superior = x

    respuesta = ""
    while respuesta != "c":
        #Generar predicción=
        if límite_inferior != límite_superior:
            predicción = random.randint(límite_inferior, límite_superior)
        else:
            predicción = límite_inferior

        # Obtener respuesta del susuario
        respuesta = input(f'mi predicción es {predicción}. Si es muy alta, ingresa (A). Si es muy baja ingresa (B). Si es correcta ingresa (C)').lower()

        if respuesta == 'a':
            límite_superior = predicción - 1
        elif respuesta == 'b':
            límite_inferior = predicción + 1

    print(f'siii! La computadora adivino tu numero correctamente: {predicción}')


adivina_el_número_computadora(10)


        #intervalo inicial: [1, 10]
        #prediccion: 6 
        #respuesta = 'a'
        #intervalo: [1, 5]

