from typing import Any

def remove(list_: list, value: Any) -> list:
    if value not in list_:
        raise ValueError("Значение не  найдено")
    list_.reverse()
    list_.remove(value)
    list_.reverse()
    return list_


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
