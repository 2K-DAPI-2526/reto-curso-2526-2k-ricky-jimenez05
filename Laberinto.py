def crear_laberinto(filas, columnas, muros):

    laberinto = [['' for _ in range(columnas)] for _ in range(filas)]

    for fila, columna in muros:
        laberinto[fila][columna] = 'X'

    laberinto[filas-1][columnas-1] = 'S'

    return laberinto


muros = ((0, 1), (0,2), (0,3), (0,4),
         (1,1),
         (2,1), (2,3),   
         (3,3),
         (4,0), (4,1), (4,2), (4,3))

laberinto = crear_laberinto(5, 5, muros)

for fila in laberinto:
    print(fila)


def resolver_laberinto(laberinto):

    filas = len(laberinto)
    columnas = len(laberinto[0])

    movimientos = [
        (0, 1, 'Derecha'),
        (1, 0, 'Abajo'),
        (0, -1, 'Izquierda'),
        (-1, 0, 'Arriba')   
    ]

    visitados = set()
    camino = []

    def dfs(fila, columna):

        if (fila < 0 or fila >= filas or
            columna < 0 or columna >= columnas or
            laberinto[fila][columna] == 'X' or
            (fila, columna) in visitados):
            return False   

        if (fila, columna) == (filas-1, columnas-1):
            return True

        visitados.add((fila, columna))

        for df, dc, nombre in movimientos:

            nueva_fila = fila + df
            nueva_columna = columna + dc

            camino.append(nombre)

            if dfs(nueva_fila, nueva_columna):
                return True

            camino.pop()

        return False


    dfs(0, 0)
    return camino


solucion = resolver_laberinto(laberinto)

print("\nSecuencia de movimientos:")
print(solucion)