def max_dollars(m, n, h, d):
    # dp[i][j] representa la máxima cantidad de dólares que se puede obtener 
    # usando los primeros i alimentos y alcanzando un nivel de salud j
    dp = [[-1] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0  # Caso base: 0 dólares si no se ha comido nada y la salud es 0
    
    for i in range(1, m + 1):
        for j in range(n + 1):
            # Opción 1: No tomar el alimento i
            dp[i][j] = dp[i - 1][j]
            
            # Opción 2: Comer el alimento i (si cabe en la salud máxima)
            if j - h[i - 1] >= 0 and dp[i - 1][j - h[i - 1]] != -1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - h[i - 1]])
            
            # Opción 3: Vender el alimento i si la salud ya es máxima
            if j == n and dp[i - 1][j] != -1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + d[i - 1])
    
    return dp[m][n] if dp[m][n] != -1 else 0

# Entrada de ejemplo
m = 6
n = 100
h = [1, 1, 1, 1, 100, 99]
d = [10, 8, 10, 10, 2, 1]

# Salida esperada: 39
dinero_max = max_dollars(m, n, h, d)
print(dinero_max)
