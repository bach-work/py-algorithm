# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

n = 5  # Количество друзей
graph_orlov = [[0 if row >= column else 1 for column in range(n)] for row in range(n)]
print(f'Количество рукопожатий: {len([el for row in graph_orlov for el in row if el != 0])}')
print(*graph_orlov, sep='\n')
