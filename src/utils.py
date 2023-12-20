


class tablero:

    import numpy as np
    from const import dim_tablero, barcos

    def __init__(self, id, dim = dim_tablero[0], tab = np.full(dim_tablero, ' '), vista = np.full(dim_tablero, '?')):
        self.id = id
        self.dim = dim
        self.tab = tab.copy()
        self.vista = vista.copy()

    def coloca_barco(self, eslora, t):
        
        import numpy as np
        import random

        ok = False
        while not ok:
            o = random.choice(['N', 'S', 'E', 'O'])
            bx = random.randint(0,self.dim-1)
            by = random.randint(0,self.dim-1)
            if (o == 'N') & (np.all(t[bx - eslora + 1 : bx + 1, by : by + 1] != 'O')) & (t[bx - eslora + 1 : bx + 1, by : by + 1].size == eslora):
                ok = True
                t[bx - eslora + 1 : bx + 1, by : by + 1] = 'O'
            elif (o == 'S') & (np.all(t[bx : bx + eslora, by : by + 1] != 'O')) & (t[bx : bx + eslora, by : by + 1].size == eslora):
                ok = True
                t[bx : bx + eslora, by : by + 1] = 'O'
            elif (o == 'E') & (np.all(t[bx : bx + 1, by : by + eslora] != 'O')) & (t[bx : bx + 1, by : by + eslora].size == eslora):
                ok = True
                t[bx : bx + 1, by : by + eslora] = 'O'
            elif (o == 'O') & (np.all(t[bx : bx + 1, by - eslora + 1 : by + 1] != 'O')) & (t[bx : bx + 1, by - eslora + 1 : by + 1].size == eslora):
                ok = True
                t[bx : bx + 1, by - eslora + 1 : by + 1] = 'O'

    def init_tablero(self):
        for i in range(4):
            self.coloca_barco(self.barcos['b1'], self.tab)
        for i in range(3):
            self.coloca_barco(self.barcos['b2'], self.tab)
        for i in range(2):
            self.coloca_barco(self.barcos['b3'], self.tab)
        self.coloca_barco(self.barcos['b4'], self.tab)






        
