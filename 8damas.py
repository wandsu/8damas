import time

inicio = time.time()
print('Backtracking: Problema das 8 damas \n')

tabuleiro = [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]

def imprimeTabuleiro(tabuleiro):
	for i in range (len(tabuleiro)):
		linha = str('')
		for j in range (len(tabuleiro[0])):
			linha += ('%d ' %tabuleiro[i][j])
		print(linha)
		
def verificaDiagonais(x,y):
        a = x-1
        b = y-1
        while(a >=0 and b >=0):
                if (tabuleiro[a][b] == 1): return False
                a -= 1
                b -= 1
        a = x-1
        b = y+1
        while(a >=0 and b < len(tabuleiro)):
                if(tabuleiro[a][b] == 1): return False
                a -= 1
                b += 1
        a = x+1
        b = y-1
        while(a < len(tabuleiro) and b >=0):
                if(tabuleiro[a][b] == 1): return False
                a += 1
                b -= 1
        a = x+1
        b = y+1
        while(a < len(tabuleiro) and b < len(tabuleiro)):
                if(tabuleiro[a][b] == 1): return False
                a += 1
                b += 1
        return True

def verificaInsercao(l,c):
	for i in range(1,len(tabuleiro)):
		#imprimeTabuleiro(tabuleiro)
		#print('\n l = {d}, c = {b}'.format(d = l, b = c))
		#print('c+i',(c+i)%8,' ',tabuleiro[l][(c+i)%8])
		#print('l+i',(l+i)%8, ' ' ,tabuleiro[(l+i)%8][c] )
		if(tabuleiro[l][(c+i)%8] == 1 or tabuleiro[(l+i)%8][c] == 1): return False
	return verificaDiagonais(l, c)

def backtracking(l,c,rc):
	if(rc==0): return True
	for i in range(len(tabuleiro)):
		tabuleiro[l][(c+i)%8] = 1
		bola = verificaInsercao(l,((c+i)%8))
		if(bola == True):
			verifica = backtracking(((l+1)%8),((c+2)%8),rc-1)
			if (verifica == True): return True
		tabuleiro[l][(c+i)%8] = 0
	return False
		#caso retorno true insere, false continua o laco
		#caso o ultimo o retorno da função 
			
imprimeTabuleiro(tabuleiro)
backtracking(0,0,len(tabuleiro))
print('\n')
imprimeTabuleiro(tabuleiro)
fim = time.time()
tempo = fim - inicio
print('Tempo de execução: ', tempo)
