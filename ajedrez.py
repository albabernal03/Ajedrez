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
            if tuple ([i,j]) in peon:
                fila.append('p')
            else:
                fila.append('x')
        tablero.append(fila)
    return tablero
  

peon = ((1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7))
tab = tablero()

for i in tab:
    print(' '.join(i))