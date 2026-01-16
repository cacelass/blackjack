import random

"""
Módulo blackjack.

Simula un juego de Blackjack con múltiples jugadores humanos
contra un único dealer. Cada jugador juega su turno de forma
secual y el dealer actúa según las reglas estándar (pide carta
hasta tener 17 o más puntos).

Las cartas se muestran con valor y palo (ej: "3 de corazones").
El objetivo es acercarse a 21 puntos sin superarlos.
"""


def valor_carta(carta):
    """
    Devuelve el valor numérico de una carta de Blackjack.

    Las figuras ('J','Q','K') valen 10. El As vale inicialmente 11.

    :param carta: Carta con valor y palo (ej: '3 de corazones')
    :type carta: str
    :return: Valor numérico de la carta
    :rtype: int
    """
    v = carta.split()[0]  # Obtener solo el valor sin palo
    if v in ['J', 'Q', 'K']:
        return 10
    if v == 'A':
        return 11
    return int(v)


def puntuacion_mano(mano):
    """
    Calcula la puntuación total de una mano de Blackjack.

    Ajusta automáticamente los Ases de 11 a 1 si la puntuación
    supera 21, evitando que el jugador se pase si es posible.

    :param mano: Lista de cartas de la mano
    :type mano: list[str]
    :return: Puntos totales de la mano
    :rtype: int
    """
    total = 0
    ases = 0
    for carta in mano:
        total += valor_carta(carta)
        if carta.startswith('A'):
            ases += 1

    while total > 21 and ases > 0:
        total -= 10
        ases -= 1

    return total


def turno_jugador(nombre, mano, baralla):
    """
    Ejecuta el turno completo de un jugador humano.

    Durante el turno, el jugador puede:
    - Pedir carta ('p')
    - Retirarse ('r')

    Cada carta que obtiene se muestra con valor y palo.

    :param nombre: Nombre del jugador
    :type nombre: str
    :param mano: Mano actual del jugador
    :type mano: list[str]
    :param baralla: Baraja de cartas disponibles
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
            print(f"Te tocó un {carta}")
        elif opcion == 'r':
            print(f"{nombre} se retira con {puntos} puntos.")
            return puntos
        else:
            print("Opción no válida.")


def main():
    """
    Función principal del juego de Blackjack.

    Flujo del juego:

    1. Crear baraja completa con palos y valores.
    2. Preguntar número de jugadores y sus nombres.
    3. Repartir 2 cartas iniciales a cada jugador y al dealer.
       El dealer muestra solo una carta.
    4. Ejecutar los turnos de cada jugador humano.
    5. Ejecutar el turno del dealer automáticamente (pide carta hasta 17).
    6. Mostrar resultados finales comparando puntuaciones.

    Cada carta se muestra con su palo y valor, y las cartas se
    extraen de la baraja para garantizar que no se repitan.
    """
    # Crear baraja
    palos = ["corazones", "diamantes", "tréboles", "picas"]
    valores = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    baralla = [f"{v} de {p}" for p in palos for v in valores]
    random.shuffle(baralla)

    # Pedir número de jugadores
    while True:
        try:
            n = int(input("¿Cuántos jugadores? "))
            if n > 0:
                break
        except ValueError:
            pass
        print("Introduce un número válido.")

    # Crear jugadores
    jugadores = {}
    for i in range(n):
        nombre = input(f"Nombre del jugador {i+1}: ")
        jugadores[nombre] = {"mano": []}

    # Dealer
    mano_dealer = []

    # Reparto inicial: 2 cartas por jugador
    for nombre, data in jugadores.items():
        carta1 = baralla.pop()
        carta2 = baralla.pop()
        data["mano"].extend([carta1, carta2])
        print(f"{nombre} recibe: {carta1}, {carta2}")

    # Reparto dealer: 1 visible, 1 oculta
    carta_visible = baralla.pop()
    carta_oculta = baralla.pop()
    mano_dealer.extend([carta_visible, carta_oculta])
    print(f"\nEl dealer muestra: {carta_visible}")

    # Turno de jugadores
    resultados = {}
    for nombre, data in jugadores.items():
        puntos = turno_jugador(nombre, data["mano"], baralla)
        resultados[nombre] = puntos

    # Turno del dealer
    puntos_dealer = puntuacion_mano(mano_dealer)
    print(f"\nMano completa del dealer: {mano_dealer} -> {puntos_dealer} puntos")

    while puntos_dealer < 17:
        carta = baralla.pop()
        mano_dealer.append(carta)
        puntos_dealer = puntuacion_mano(mano_dealer)
        print(f"El dealer coge {carta} -> {puntos_dealer} puntos")

    # Resultados finales
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
