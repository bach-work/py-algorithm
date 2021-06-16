# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

def get_graph(n: int):
    """Делает граф"""
    g = [[] for _ in range(n)]
    for row in range(n):
        g[row] = [column for column in range(n) if row != column and row not in g[column]]
    return g


n = 5  # Количество вершин
landgraf = get_graph(5)
print(*landgraf, sep='\n')


def move_dfs(graph: list, vertex_start: int, visited: list = None, path: list = []):
    """Обходит граф в глубину и возвращает путь"""
    if visited is None:
        visited = [False] * n
    visited[vertex_start] = True
    path.append(vertex_start)
    for i in graph[vertex_start]:
        if not visited[i]:
            move_dfs(graph, i, visited, path)
    return path


print(f'Путь обхода: {move_dfs(landgraf, 0)}')
