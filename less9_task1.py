# 1. Определить количество подстрок в строке
import hashlib


def calc(s: str):
    """
    Строит словарь уникальных подстрок с их хэшами
    и возвращает количество подстрок
    """
    def _hash_(sub):
        """Возвращает хэш подстроки"""
        return hashlib.sha1(sub.encode('utf-8')).hexdigest()

    return len({_hash_(sub): sub for sub in (s[i: i+j] for i in range(len(s)) for j in range(len(s) - i + 1))
                if 0 < len(sub) < len(s)})


count = calc(input('Введите строку: '))
print('Количество уникальных подстрок: {}'.format(count))
