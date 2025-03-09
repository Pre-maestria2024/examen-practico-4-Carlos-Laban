from collections import defaultdict

def max_groups(n, k, edges):
    if k == 0 or n == 0:
        return 0
    
    # Construcción del árbol como un diccionario de listas de adyacencia
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # DFS para contar cuántos grupos se pueden formar
    def dfs(node, parent):
        sizes = []
        for neighbor in tree[node]:
            if neighbor != parent:
                sizes.append(dfs(neighbor, node))
        
        # Ordenar los tamaños de las subrutas de mayor a menor
        sizes.sort(reverse=True)
        
        # Contar cuántos grupos de tamaño k se pueden formar
        total_groups = 0
        current_size = 1  # La cabaña actual
        
        for size in sizes:
            if current_size + size >= k:
                total_groups += 1
                current_size = 0
            else:
                current_size += size
        
        return current_size + 1  # Retornar el tamaño de la subruta
    
    # Llamada inicial de DFS desde la raíz 0
    dfs(0, -1)
    
    return dfs(0, -1) // k

# Entrada de ejemplo
n = 34
k = 3
edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (2, 6), (6, 7), (0, 8), (8, 9),
    (9, 10), (10, 11), (11, 12), (12, 13), (12, 14), (8, 15), (15, 16), (16, 17),
    (17, 18), (15, 19), (19, 20), (20, 21), (20, 22), (20, 23), (21, 24),
    (21, 25), (21, 26), (8, 27), (27, 28), (28, 29), (28, 30), (29, 31),
    (31, 32), (31, 33)
]

# Salida esperada: 8
print(max_groups(n, k, edges))

