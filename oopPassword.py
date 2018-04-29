import string
import random


def passGen(size = 8 , chars = string.ascii_letters + string.digits + string.punctuation):
    return "".join(random.choice(chars) for _ in range(size))

print(passGen(int(input("How many characters in your password?"))))
