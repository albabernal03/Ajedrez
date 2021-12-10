def tablero():
    tablero = []
    for i in range(6):
        fila = []
    for j in range(8):
        fila.append('X')
        tablero.append(fila)
    return tablero

tab = tablero()