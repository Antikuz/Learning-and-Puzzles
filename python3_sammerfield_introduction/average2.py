#!/usr/bin/env python3
numbers = []
total = 0

def get_mediana(value):
    x = 0
    mediana = int(value/2)
    while value > 0:
        if x == 0:
            x = 1
        elif x == 1:
            x = 0
        value -= 1
    if x == 1:
        mediana = numbers [mediana]
    if x == 0:
        x = numbers [mediana]
        y = numbers [mediana - 1]
        mediana = (x+y)/2
    return mediana
while True:
    answer = input ("Введите число или нажмите Enter для подсчета:")
    if not answer:
        break
    try:
        number = int(answer)
    except ValueError as err:
        print("Неправильный ввод, пожалуйста введите целое число")
        continue
    total += number
    numbers.append (number) 
highest = numbers[0]
for highestcount in numbers:
    if highestcount > highest:
        highest = highestcount
        
lowest = numbers[0]
for lowestcount in numbers:
    if lowestcount < lowest:
        lowest = lowestcount
count = total//len(numbers)
print (numbers)
print ("Всего цифр:", len(numbers))
print ("Всего цифр:", len(numbers),"Наименьшее число:", lowest,"Наибольшее число:", highest,"Среднее значение:", count, 'Медиана:', get_mediana(len(numbers)))