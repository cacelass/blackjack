from blackjack.main import puntuacion_mano, valor_carta


def test_valor_carta_numeros():
    assert valor_carta('2') == 2
    assert valor_carta('10') == 10
    assert valor_carta('7') == 7


def test_valor_carta_figuras():
    assert valor_carta('J') == 10
    assert valor_carta('Q') == 10
    assert valor_carta('K') == 10


def test_valor_carta_as():
    assert valor_carta('A') == 11


def test_puntuacion_mano_sin_as():
    mano = ['10', '7']
    assert puntuacion_mano(mano) == 17


def test_puntuacion_mano_con_un_as_sin_ajuste():
    mano = ['A', '8']
    assert puntuacion_mano(mano) == 19


def test_puntuacion_mano_con_un_as_con_ajuste():
    mano = ['A', '9', '5']
    # 11 + 9 + 5 = 25 → As vale 1 → total 15
    assert puntuacion_mano(mano) == 15


def test_puntuacion_mano_con_dos_ases():
    mano = ['A', 'A', '9']
    # 11 + 11 + 9 = 31
    # ajuste: 21
    assert puntuacion_mano(mano) == 21


def test_puntuacion_mano_se_pasa():
    mano = ['K', '9', '5']
    assert puntuacion_mano(mano) == 24
