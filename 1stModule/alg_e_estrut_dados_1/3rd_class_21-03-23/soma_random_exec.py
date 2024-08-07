import random

numero = int(input("insira um numero entre 1 e 10: "))
random_numero = 0
random_num = 0
while numero != random_num:
    random_num = random.randint(1,10)
    random_numero += random_num
    print(random_numero)