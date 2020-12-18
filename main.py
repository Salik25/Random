import random

n = int(input('Введите кол-во бочонков: '))
s = []
for i in range(n):  # заполнение списка бочонками с рандомными числами которые не повторяються
    ran = random.randint(1, n)
    while len(s) != n:
        ran = random.randint(1, n)
        if ran not in s:
            s.append(ran)

while True:  # цикл для жеребьевки
    print(s.pop(0))  # удаление бочонка
    if len(s) == 0:
        print('Бочонки закончились')
        quit()
