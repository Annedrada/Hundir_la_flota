

import numpy as np
import random
from utils import tablero



def dispara_jugador(t):

    print('¿Donde disparas?')
    l = ''
    while (not l.isdigit) or (l not in [str(i+1) for i in range(t.dim)]):
        l = input('_linea:')
    l = int(l) - 1
    c = ''
    while (not c.isdigit) or (c not in [str(i+1) for i in range(t.dim)]):
        c = input('_columna:')
    c = int(c) - 1

    if t.tab[l, c] == 'O':
        print('¡Hurra! ¡Disparaste a un barco enemigo!')
        print()
        t.tab[l, c] = 'X'
        t.vista[l, c] = 'X'
        return False
    elif t.tab[l, c] == ' ':
        t.tab[l, c] = '-'
        t.vista[l, c] = '-'
        return True
    return True



def dispara_maquina(t):

    l, c = random.randint(0,t.dim-1), random.randint(0,t.dim-1)
    
    if t.tab[l, c] == 'O':
        print('¡La máquina disparó a un barco tuyo! X_X')
        t.tab[l, c] = 'X'
        t.vista[l, c] = 'X'
        return False
    elif t.tab[l, c] == ' ':
        t.tab[l, c] = '-'
        t.vista[l, c] = '-'
        return True
    return True



def perdio(tablero_de_cualquiera):

    if np.any(tablero_de_cualquiera.tab == 'O'):
        return False
    return True



def nuevo_juego():

    def muestra_Tjugador():
        print()
        print('Vista de tu tablero ahora:')
        print(tj.tab)
    
    def muestra_Tenemigo():
        print()
        print('Vista del tablero enemigo:')
        print(tm.vista)

    
    # Eligimos dificultad

    dif = input('Elige dificultad - número de intentos permitidos de la maquina [1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10]:')
    while (not dif.isdigit) or (dif not in ['1','2','3','4','5','6','7','8','9','10']):
        dif = input('No entiendo, vuelve a introducir la opción >')
    dif = int(dif) 
    

    # Inicializamos los dos tableros

    tj = tablero('jugador')
    tj.init_tablero()
    tm = tablero('máquina')
    tm.init_tablero()


    # Jugamos

    jugando = True
    while jugando:

        mi_turno = True

        # Mostramos las opciones en cada input de usuario y le preguntamos que quiere hacer

        print("""
1 - Dispara  |  2 - Muestra tu tablero  |  3 - Muestra el tablero enemigo  |  4 - Salir""")
        opc = input('> ')
        while (not opc.isdigit) or (opc not in ['1','2','3','4','5','6','7','8','9','10']):
            opc = input('No entiendo, vuelve a introducir la opción >')
        opc = int(opc)
        if opc == 2:
            muestra_Tjugador()
        elif opc == 3:
            muestra_Tenemigo()
        elif opc == 4:
            jugando = False
            return True
        elif opc == 1:

            # Si elige jugar, jugamos

            while jugando and mi_turno:
                stop = dispara_jugador(tm)
                if stop and not perdio(tm):
                    print('Fallaste. Ahora le toca a la máquina.')
                    print()
                    mi_turno = False
                if perdio(tm):
                    muestra_Tenemigo()    
                    print("""
                        ┓┏              ┓          ╻╻╻
                        ┣┫┏┓┏  ┏┓┏┓┏┓┏┓┏┫┏┓┏┓┏┓┏┓  ┃┃┃
                        ┛┗┗┻┛  ┗┫┗┻┛┗┗┻┗┻┗┛┗┛┗┛┗┛  •••
                                ┛                     """)
                    mi_turno = False
                    jugando = False
            
            turno_maq = True
            intento = 1
            while jugando and turno_maq:
                stop = dispara_maquina(tj)
                if stop and not perdio(tj):
                    print('¡Tranquilo! La máquina disparó pero falló :)')
                    intento += 1
                    if intento > dif:
                        turno_maq = False
                if perdio(tj):
                    muestra_Tjugador()
                    print("""
                        ┓┏            ┓• ┓          ┓•    
                        ┣┫┏┓┏  ┏┓┏┓┏┓┏┫┓┏┫┏┓     ┏┓┏┫┓┏┓┏ 
                        ┛┗┗┻┛  ┣┛┗ ┛ ┗┻┗┗┻┗┛•••  ┗┻┗┻┗┗┛┛•
                               ┛                      """)
                    turno_maq = False
                    jugando = False





print("""
             ┓┏  ┳┳  ┳┓  ┳┓  ┳  ┳┓      ┓   ┏┓      ┏┓  ┓   ┏┓  ┏┳┓  ┏┓         
    ┏━┛      ┣┫  ┃┃  ┃┃  ┃┃  ┃  ┣┫      ┃   ┣┫      ┣   ┃   ┃┃   ┃   ┣┫      ┏━┛
             ┛┗  ┗┛  ┛┗  ┻┛  ┻  ┛┗      ┗┛  ┛┗      ┻   ┗┛  ┗┛   ┻   ┛┗         
                                                                            

            ¡Bienvenido!
            
            Vamos a jugar a hundir la flota. 

            Tu y tu oponente(la máquina) tenéis cada uno un tablero de 10 x 10 con los siguientes barcos:      
                * 4 barcos de 1 posición de eslora
                * 3 barcos de 2 posiciones de eslora
                * 2 barcos de 3 posiciones de eslora
                * 1 barco de 4 posiciones de eslora
            El juego va por turnos y empiezas tu.
            En cada turno disparas a una coordenada (X, Y) del tablero adversario. 
            ¡Si aciertas, te vuelve a tocar!. En caso contrario, le toca a la máquina.
            En los turnos de la máquina, si acierta, también le vuelve a tocar.
            Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.
      
            ¡Mucha suerte!

""")

salir = False
o = 0

while (o != 2) and (not salir):
    o = ''
    print("""
            1 - Nuevo juego
            2 - Salir""")
    while (not o.isdigit) or (o not in ['1', '2']):
        o = input("""
                > """)
    o = int(o)
    if o == 1:
        salir = nuevo_juego()
    