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
            elif tuple ([i,j]) in torre:
                fila.append('t')
            elif tuple ([i,j]) in alfil:
                fila.append('a')
            elif tuple ([i,j]) in caballo:
                fila.append('c')
            elif tuple ([i,j]) in rey:
                fila.append('#')
            elif tuple ([i,j]) in reina:
                fila.append('r')
            else:
                fila.append(' ')
        tablero.append(fila)
    return tablero
  

peon = ((1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7))
torre = ((0,0), (0,7), (5,0), (5,7))
alfil = ((0,2), (0,5), (5,2), (5,5))
caballo = ((0,1), (0,6), (5,1), (5,6))
rey = ((0,3), (5,3))
reina = ((0,4), (5,4))
tab = tablero()

def mostrar_tablero (t):
    for i in t:
        print(' '.join(i))
 

opcion = 1

while opcion != 2:

    print('.:MENU:.')
    print('1: Mover ficha')
    print('2: Finalizar')
    
    opcion = int(input('Seleccione una opcion:'))

    if opcion == 1:
        filaI = int(input('Ingrese la fila de la ficha a mover:'))
        columnaI = int(input('Ingrese la columna de la ficha que desea mover:'))

        if filaI >= 0 and filaI <= 5 and columnaI >= 0 and columnaI <=7:

            if tab[filaI][columnaI] != ' ':
                filaF = int(input('Ingrese la fila a donde desea mover la ficha:'))
                columnaF = int(input('Ingrese la columna donde desea mover la ficha:'))

                if filaF >= 0 and filaF <= 5 and columnaF >= 0 and columnaF <= 7:
                    print('Puede mover ficha')
                    pieza = tab[filaI][columnaI]

                else:
                    print('Las posiciones indicada no se encuentra del tablero') 

            else:
                print('No hay ficha en esta posición')

        else:
            print('Las posiciones indicadas no se encuentran dentro del tablero')

    elif opcion == 2:
        print('FIN DEL JUEGO')
    else:
        print('Opción inválida!')

    
