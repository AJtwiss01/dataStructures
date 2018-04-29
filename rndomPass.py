import random

choices = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"
passlen  = 8

password = "".join(random.sample(choices, passlen))

print(password)
