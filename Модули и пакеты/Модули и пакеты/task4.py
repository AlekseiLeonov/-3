import random
from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    eagle = 0 # Количество выпавших орлов
    tails = 0 # Количество выпавших решек
    for _ in range(count):
        side = random.choice(coin) # выбор стороны монеты
        if side == EAGLE:
            eagle += 1
        else:
            tails += 1
    if eagle < tails:
        result = eagle / tails
    else:
        result = tails / eagle
    list_freq.append(result)

print(list_freq)
