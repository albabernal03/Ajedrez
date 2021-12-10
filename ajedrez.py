#peon ---> p
#torre ----> t
#alfil ----> a
#caballo ---> c
#rey ----> #
#reina ----> r

def tablero():
    tablero = []
    for i in range(6):
        fila = []
    for j in range(8):
        fila.append('X')
        tablero.append(fila)
    return tablero

tab = tablero()

for i in tab:
    print(' '.join(i))