import random


def jugar():  #Función

    usuario = input("escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return 'Empate!!!'

    if gano_el_jugador (usuario, computadora):
        return 'Ganaste!!!'

    return 'Perdiste!!!'


def gano_el_jugador (jugador, oponente):
    #Retornar true si gana el jugador
    #piedra gana a tijera (pi>ti).
    #tijera le gana a papel (ti>pa).
    #papel le gana a piedra (pa>pi).
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador =='ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())
    


    
