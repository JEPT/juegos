def crearMatriz(n, m) :
    matrix = [ None ] * n
    for i in range (0,n):
          matrix[i] = [' '] * m
    return matrix
def crearMatrizNum(n, m) :
    matrix = [ None ] * n
    for i in range (0,n):
          matrix[i] = [0] * m
          matrix[i][0] = i+1
    return matrix
    
def printMatriz(l) :
    for i in range (0,len (l)):
        contador=""
        for j in range (0,len(l[0])):
            contador+=str(l[i][j])
        print (contador)

 
def pri(A, B, C) : 
     for i in range (0,len(A)):
          for j in range (0,len(A[i])):
              print (A[i][j], end='')
          for j in range (0,len(B[i])):
              print (B[i][j], end='')
          for j in range (0,len(C[i])):
              print (C[i][j], end='')
          print ("")

     
def hanoi (a, b ,c, n,Matris):
    if n > 0 :
        hanoi(a, c, b, n-1,Matris)
        print (a, " => ", c)
        pos = len(Matris) - 1
        for i in range (0, len(Matris)):
            if Matris[i][a] > 0 :
                pos = i
                break

        pos2 = len(Matris) - 1
        for i in range (0, len(Matris)):
            if Matris[i][c] > 0 :
                pos2 = i -1
                break
            
        Matris[pos2][c] = Matris[pos][a]
        Matris[pos][a] = 0
        
        A = Hanoi(Matris, 0) 
        B = Hanoi(Matris, 1) 
        C = Hanoi(Matris, 2) 
        pri(A, B, C) 
        hanoi(b, a, c, n-1, Matris )


def Hanoi(matri, palo) :
     may = len (matri)
     str= crearMatriz (len(matri), 2*may+1)
     for i in range (0,len(matri)):
        n = matri[i][palo] - 1
        if n >= 0 :
            for p in range (0, len(matri)-(n)):
                str[i][p] = ' '
            for q in range (0, 2*n+1):
                str[i][p] = '='
                p += 1
     return  str

n =  int(input())
Matris= crearMatrizNum(n, 3)

printMatriz(Matris)
hanoi (0 , 1 , 2, n, Matris)
