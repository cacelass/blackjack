import random

"""
Módulo blackjack.

Implementa una simulación de Blackjack con múltiples jugadores humanos
contra un único dealer. Cada jugador juega su turno de forma secuencial
y el dealer actúa según las reglas estándar (pide carta hasta 17).

El objetivo es acercarse a 21 puntos sin superarlos.
"""


def valor_carta(carta):
    """
    Devuelve el valor numérico de una carta en Blackjack.

    Las figuras (J, Q, K) valen 10 puntos.
    El As vale inicialmente 11 puntos (ajustable posteriormente).

    :param carta: Representación de la carta ('A', 'K', 'Q', 'J', '2'...'10')
    :type carta: str
    :return: Valor numérico de la carta
    :rtype: int
    """
    if carta in ['J', 'Q', 'K']:
        return 10
    if carta == 'A':
        return 11
    return int(carta)


def puntuacion_mano(mano):
    """
    Calcula la puntuación total de una mano de Blackjack.

    Ajusta automáticamente el valor de los Ases de 11 a 1 si la puntuación
    supera 21, evitando que el jugador se pase cuando sea posible.

    :param mano: Lista de cartas en la mano del jugador
    :type mano: list[str]
    :return: Puntuación total de la mano
    :rtype: int
    """
    total = 0
    ases = 0

    for carta in mano:
        total += valor_carta(carta)
        if carta == 'A':
            ases += 1

    while total > 21 and ases > 0:
        total -= 10
        ases -= 1

    return total


def turno_jugador(nombre, mano, baralla):
    """
    Gestiona el turno completo de un jugador.

    El jugador puede pedir cartas o retirarse. El turno finaliza
    cuando el jugador se retira o supera los 21 puntos.

    :param nombre: Nombre del jugador
    :type nombre: str
    :param mano: Mano actual del jugador
    :type mano: list[str]
    :param baralla: Baraja de cartas disponible
    :type baralla: list[str]
    :return: Puntuación final del jugador
    :rtype: int
    """
    while True:
        puntos = puntuacion_mano(mano)
        print(f"\nJugador {nombre}")
        print(f"Mano: {mano} -> {puntos} puntos")

        if puntos > 21:
            print("Te pasaste de 21.")
            return puntos

        opcion = input("Pedir carta (p) o retirarte (r)? ").lower()

        if opcion == 'p':
            carta = baralla.pop()
            mano.append(carta)
            print(f"Carta obtenida: {carta}")
        elif opcion == 'r':
            print(f"{nombre} se retira con {puntos} puntos.")
            return puntos
        else:
            print("Opción no válida.")


def main():
    """
    Función principal del juego de Blackjack.

    Solicita el número de jugadores y sus nombres, reparte las cartas
    iniciales, gestiona los turnos de cada jugador y finalmente ejecuta
    el turno del dealer y muestra los resultados finales.
    """
    baralla = ['A','K','Q','J','10','9','8','7','6','5','4','3','2'] * 4
    random.shuffle(baralla)

    while True:
        try:
            n = int(input("¿Cuántos jugadores? "))
            if n > 0:
                break
        except ValueError:
            pass
        print("Introduce un número válido.")

    jugadores = {}

    for i in range(n):
        nombre = input(f"Nombre del jugador {i+1}: ")
        jugadores[nombre] = {"mano": []}

    mano_dealer = []

    for jugador in jugadores.values():
        jugador["mano"].append(baralla.pop())
        jugador["mano"].append(baralla.pop())

    mano_dealer.append(baralla.pop())
    print(f"\nEl dealer muestra: {mano_dealer[0]}")

    resultados = {}
    for nombre, data in jugadores.items():
        puntos = turno_jugador(nombre, data["mano"], baralla)
        resultados[nombre] = puntos

    mano_dealer.append(baralla.pop())
    puntos_dealer = puntuacion_mano(mano_dealer)
    print(f"\nMano del dealer: {mano_dealer} -> {puntos_dealer} puntos")

    while puntos_dealer < 17:
        carta = baralla.pop()
        mano_dealer.append(carta)
        puntos_dealer = puntuacion_mano(mano_dealer)
        print(f"El dealer coge {carta} -> {puntos_dealer}")

    print("\nRESULTADOS FINALES")
    for nombre, puntos in resultados.items():
        if puntos > 21:
            print(f"{nombre}: pierde (se pasó)")
        elif puntos_dealer > 21 or puntos > puntos_dealer:
            print(f"{nombre}: GANA")
        elif puntos == puntos_dealer:
            print(f"{nombre}: EMPATA")
        else:
            print(f"{nombre}: pierde")


if __name__ == "__main__":
    main()
