import readchar

class Sokoban:
    #Variables Globales
    mapa = []
    jalar = False
    
    def load_game_mapa(self):
        file = open('0.txt','r')
        for line in file:
            fila = []
            for c in line[: - 1]:
                fila.append(int(c))
            self.mapa.append(fila)

    fila = 2
    columna = 1

    def imprimir_mapa(self): #Imprimir mapa
        for f in range(8):
            linea=''
            for c in range(10):
                linea += str(self.mapa[f][c]) + '  '
            print linea
            
    def mover_derecha(self):
        if self.mapa[self.fila][self.columna-1]==3 and self.mapa[self.fila][self.columna+1]==1 and self.jalar==True:
            self.mapa[self.fila][self.columna+1]=0
            self.mapa[self.fila][self.columna-1]=1
            self.mapa[self.fila][self.columna]=3
            self.columna+=1

        elif self.mapa[self.fila][self.columna+1]==1 and self.mapa[self.fila][self.columna-1]==5 and self.jalar==True:
            self.mapa[self.fila][self.columna+1]=0
            self.mapa[self.fila][self.columna-1]=4
            self.mapa[self.fila][self.columna]=3
            self.columna+=1

        elif self.mapa[self.fila][self.columna+1]==1: #Validar espacio
            self.mapa[self.fila][self.columna+1]=0 #Mover monito
            self.mapa[self.fila][self.columna]=1 #espacio
            self.columna+=1 #Actualizamos posicion

        elif self.mapa[self.fila][self.columna+1]==3 and self.mapa[self.fila][self.columna+2]==1:
            self.mapa[self.fila][self.columna+2]=3
            self.mapa[self.fila][self.columna+1]=0
            self.mapa[self.fila][self.columna]=1
            self.columna+=1

        elif self.mapa[self.fila][self.columna+1]==3 and self.mapa[self.fila][self.columna+2]==4:
            self.mapa[self.fila][self.columna+2]=5
            self.mapa[self.fila][self.columna+1]=0
            self.mapa[self.fila][self.columna]=1
            self.columna+=1

    def mover_izquierda(self):
        if self.mapa[self.fila][self.columna+1]==3 and self.mapa[self.fila][self.columna-1]==1 and self.jalar==True:
            self.mapa[self.fila][self.columna-1]=0
            self.mapa[self.fila][self.columna+1]=1
            self.mapa[self.fila][self.columna]=3
            self.columna-=1

        elif self.mapa[self.fila][self.columna-1]==1 and self.mapa[self.fila][self.columna+1]==5 and self.jalar==True:
            self.mapa[self.fila][self.columna-1]=0
            self.mapa[self.fila][self.columna+1]=4
            self.mapa[self.fila][self.columna]=3
            self.columna-=1

        elif self.mapa[self.fila][self.columna-1]==1: #Validar espacio
            self.mapa[self.fila][self.columna-1]=0 #Mover monito
            self.mapa[self.fila][self.columna]=1 #espacio
            self.columna-=1 #Actualizamos posicion

        elif self.mapa[self.fila][self.columna-1]==3 and self.mapa[self.fila][self.columna-2]==1:
            self.mapa[self.fila][self.columna-2]=3
            self.mapa[self.fila][self.columna-1]=0
            self.mapa[self.fila][self.columna]=1
            self.columna-=1

        elif self.mapa[self.fila][self.columna-1]==3 and self.mapa[self.fila][self.columna-2]==4:
            self.mapa[self.fila][self.columna-2]=5
            self.mapa[self.fila][self.columna-1]=0
            self.mapa[self.fila][self.columna]=1
            self.columna-=1
            
    def mover_arriba(self):
        if self.mapa[self.fila+1][self.columna]==3 and self.mapa[self.fila-1][self.columna]==1 and self.jalar==True:
            self.mapa[self.fila-1][self.columna]=0
            self.mapa[self.fila+1][self.columna]=1
            self.mapa[self.fila][self.columna]=3
            self.fila-=1

        elif self.mapa[self.fila-1][self.columna]==1 and self.mapa[self.fila+1][self.columna]==5 and self.jalar==True:
            self.mapa[self.fila-1][self.columna]=0
            self.mapa[self.fila+1][self.columna]=4
            self.mapa[self.fila][self.columna]=3
            self.fila-=1

        elif self.mapa[self.fila-1][self.columna]==1: #Validar espacio
            self.mapa[self.fila-1][self.columna]=0 #Mover monito
            self.mapa[self.fila][self.columna]=1 #espacio
            self.fila-=1 #Actualizamos posicion

        elif self.mapa[self.fila-1][self.columna]==3 and self.mapa[self.fila-2][self.columna]==1:
            self.mapa[self.fila-2][self.columna]=3
            self.mapa[self.fila-1][self.columna]=0
            self.mapa[self.fila][self.columna]=1
            self.fila-=1

        elif self.mapa[self.fila-1][self.columna]==3 and self.mapa[self.fila-2][self.columna]==4:
            self.mapa[self.fila-2][self.columna]=5
            self.mapa[self.fila-1][self.columna]=0
            self.mapa[self.fila][self.columna]=1
            self.fila-=1

    def mover_abajo(self):
        if self.mapa[self.fila-1][self.columna]==3 and self.mapa[self.fila+1][self.columna]==1 and self.jalar==True:
            self.mapa[self.fila+1][self.columna]=0
            self.mapa[self.fila-1][self.columna]=1
            self.mapa[self.fila][self.columna]=3
            self.fila+=1

        elif self.mapa[self.fila+1][self.columna]==1 and self.mapa[self.fila-1][self.columna]==5 and self.jalar==True:
            self.mapa[self.fila+1][self.columna]=0
            self.mapa[self.fila-1][self.columna]=4
            self.mapa[self.fila][self.columna]=3
            self.fila+=1

        elif self.mapa[self.fila+1][self.columna]==1: #Validar espacio
            self.mapa[self.fila+1][self.columna]=0 #Mover monito
            self.mapa[self.fila][self.columna]=1 #espacio
            self.fila+=1 #Actualizamos posicion

        elif self.mapa[self.fila+1][self.columna]==3 and self.mapa[self.fila+2][self.columna]==1:
            self.mapa[self.fila+2][self.columna]=3
            self.mapa[self.fila+1][self.columna]=0
            self.mapa[self.fila][self.columna]=1
            self.fila+=1

        elif self.mapa[self.fila+1][self.columna]==3 and self.mapa[self.fila+2][self.columna]==4:
            self.mapa[self.fila+2][self.columna]=5
            self.mapa[self.fila+1][self.columna]=0
            self.mapa[self.fila][self.columna]=1
            self.fila+=1

objeto=Sokoban()
objeto.load_game_mapa()

while True:
    objeto.imprimir_mapa()
    print objeto.jalar
    print 'Mono: '+str(objeto.fila)+' '+str(objeto.columna) #Imprimir posicion
    movimiento=readchar.readchar() #a-d-w-s:
    print '\n'
    if movimiento=='d':
        objeto.mover_derecha()
    elif movimiento=='a':
        objeto.mover_izquierda()
    elif movimiento=='w':
        objeto.mover_arriba()
    elif movimiento=='s':
        objeto.mover_abajo()
    elif movimiento == 'l':
        objeto.jalar = True
    elif movimiento == 'm':
        objeto.jalar = False
        
