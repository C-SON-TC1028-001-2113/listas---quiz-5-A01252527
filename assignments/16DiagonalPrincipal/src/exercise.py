

def diagonal(matriz):
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
    return diagonal

def mati (Y,X):
    matriz = []
    if Y == X:
        for i in range(Y):
            matriz.append([])
            for j in range (Y):
                matriz[i].append(int(input()))
    return matriz

def main():
    X = int(input())
    Y = int(input())
    if X != Y:
        print("La matriz no es cuadrada")
    else:
        MATRIZ = mati(X, Y)
        print(diagonal(MATRIZ))


if __name__=='__main__':
    main()
