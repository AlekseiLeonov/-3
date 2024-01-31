import random

def three_random_number() -> list[int]:
    list_numbers =[None] * 3
    for i in range(3):
        num = random.randint(0, 9)
        list_numbers[i] = num
    list_numbers = ''.join(map(str, list_numbers))
    return list_numbers

print(three_random_number())