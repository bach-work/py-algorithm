# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]  # Граф из урока


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    parent_dict = {i: [] for i in range(length)}

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    parent_dict[i] = parent_dict[start][:]
                    parent_dict[i].append(start)

        parent_dict[start].append(start)
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    return cost, parent_dict


c, d = dijkstra(graph, 0)
print(f'Кратчайшие пути: {c}')
print('-'*20)
for k, v in d.items():
    print(f'Вершина {k}, путь: {v}')

# Будь проклят этот Дейкстра со своим алгоритмом
# У меня чуть мозг не лопнул, пока я эту задачу решал