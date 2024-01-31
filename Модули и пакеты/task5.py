import random
from random import sample
def get_random_password() -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" # Полный список используемых символов
    password = random.sample(alphabet, 8)
    password = "".join(password)
    return password


print(get_random_password())
