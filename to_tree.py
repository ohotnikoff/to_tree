"""
Написать функцию, строящую дерево по списку пар id (id подителя, id потомка),
где None - id корневого узла.
"""

source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a21'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]


expected = {
    'a': {'a1': {}, 'a2': {'a21': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}


def find_key(d, key):
    """
    Рекурсия. Поиск ключа в словаре.
    """
    if key in d.keys():
        return d
    else:
        for item in d.values():
            find_item = find_key(item, key)
            if find_item:
                return find_item


def to_tree(source):
    """
    Функция, строящая дерево по списку пар id.
    """
    output = {}

    for a in source:
        if a[0] is None:
            output[a[1]] = {}
        else:
            data = find_key(output, a[0])
            if data is not None:
                data[a[0]][a[1]] = {}

    return output


print(to_tree(source))
print(to_tree(source) == expected)
