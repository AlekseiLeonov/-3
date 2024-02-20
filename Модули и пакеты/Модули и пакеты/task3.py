import random
def get_unique_list_numbers() -> list[int]:
    unique_list = [None]*15
    for i in range(15):
        num = random.randint(-15, 15)
        while num in unique_list:
            num = random.randint(-15, 15)
        unique_list[i] = num
    return unique_list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
