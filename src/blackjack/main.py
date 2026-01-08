import random
'''Simulación simple de un juego de Blackjack entre un jugador y un dealer. El jugador puede pedir cartas o retirarse, y el dealer sigue reglas fijas.
El objetivo es acercarse lo más posible a 21 sin pasarse.'''
def valor_carta(carta):
    '''Devuelve el valor numérico de una carta en Blackjack.'''
    if carta in ['J', 'Q', 'K']:
        return 10
    if carta == 'A':
        return 11
    return int(carta)

def puntuacion_mano(man):
    '''Calcula la puntuación total de una mano en Blackjack, ajustando el valor de los Ases según sea necesario.'''
    total = 0
    ases = 0

    for carta in man:
        total += valor_carta(carta)
        if carta == 'A':
            ases += 1

    while total > 21 and ases > 0:
        total -= 10
        ases -= 1

    return total


def main():
    '''Función principal para ejecutar el juego de Blackjack.'''
    baralla = ['A','K','Q','J','10','9','8','7','6','5','4','3','2'] * 4
    random.shuffle(baralla)

    mano = []
    mano_dealer = []

    '''Repartir dos cartas iniciales para el jugador y una para el dealer'''
    mano.append(baralla.pop())
    mano.append(baralla.pop())
    mano_dealer.append(baralla.pop())

    while True:
        '''Función principal para ejecutar el juego de Blackjack.'''
        puntos = puntuacion_mano(mano)
        print(f"\nTu mano: {mano} -> {puntos} puntos")

        if puntos > 21:
            print("Pasaste de 21. Pierdes.")
            break
        print(f"Solo puedes ver una carta del dealer, es {puntuacion_mano(mano_dealer)}")
        opcion = input("Quieres pedir carta (p) o retirarte (r)? ").lower()

        if opcion == 'p':
            carta = baralla.pop()
            mano.append(carta)
            print(f"Cogiste: {carta}")
        elif opcion == 'r':
            print(f"Te retiraste con {puntos} puntos.")
            # Turno del dealer

            mano_dealer.append(baralla.pop())
            puntos_dealer = puntuacion_mano(mano_dealer)
            print(f"La mano del dealer: {mano_dealer} -> {puntos_dealer} puntos")

            while puntos_dealer < 17:
                '''El dealer debe pedir carta si tiene menos de 17 puntos.'''
                carta = baralla.pop()
                mano_dealer.append(carta)
                puntos_dealer = puntuacion_mano(mano_dealer)
                print(f"El dealer coge: {carta} -> {puntos_dealer} puntos")

            if puntos_dealer > 21:
                print("El dealer pasó de 21. ¡Ganaste!")
            elif puntos > puntos_dealer:
                print("¡Ganaste!")
            else:
                print("¡Perdiste!")

            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
