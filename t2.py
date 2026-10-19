
PUNTOS_MINIMOS = 23

movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def imprime(mat):
    for x in mat:
        print(x)
    print()

def valido(lab, res, f, c):
    if f >= len(lab):
        return False
    if f < 0:
        return False
    if c >= len(lab[0]):
        return False
    if c < 0:
        return False
    if res[f][c] == 1:        
        return False
    if lab[f][c] == 0:        
        return False
    return True


def laberinto4(lab, res, f, c, puntos):
  
    res[f][c] = 1


    if f == 0 and c == 0:
        if puntos >= PUNTOS_MINIMOS:
            return True
    else:
   
        for df, dc in movimientos:
            nf = f + df
            nc = c + dc
            if valido(lab, res, nf, nc):
                if laberinto4(lab, res, nf, nc, puntos + lab[nf][nc]):
                    return True


    res[f][c] = 0
    return False


def main():
    lab = [
        [1, 1, 1, 3, 0, 1, 1, 1, 4],
        [3, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 3, 1, 1],
        [3, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 3, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 1, 0, 0, 4],
        [1, 1, 3, 1, 0, 1, 1, 1, 1],
    ]
    filas = len(lab)
    columnas = len(lab[0])

    original = [fila[:] for fila in lab]
    original[filas - 1][0] = 'I'
    original[0][0] = 'F'
    print("=== LABERINTO ORIGINAL ===")
    imprime(original)

    res = []
    for i in range(filas):
        res.append([0] * columnas)

    salio = laberinto4(lab, res, filas - 1, 0, lab[filas - 1][0])

    if salio:
        total = 0
        for i in range(filas):
            for j in range(columnas):
                if res[i][j] == 1:
                    total = total + lab[i][j]
        print("¡El ratón logró salir del laberinto! Puntos acumulados:", total)
        print()
        
        solucion = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                if res[i][j] == 1:
                    fila.append(lab[i][j])
                else:
                    fila.append(0)
            solucion.append(fila)
        print("=== MATRIZ SOLUCIÓN ===")
        imprime(solucion)
    else:
        print("El ratón NO logró salir con", PUNTOS_MINIMOS, "puntos o más.")


main()