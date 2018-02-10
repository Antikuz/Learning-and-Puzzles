#!/usr/bin/env python3
numbers = []
total = 0
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
print (numbers)
print ("Всего цифр:", len(numbers),"Наименьшее число:", lowest,"Наибольшее число:", highest,"Среднее значение:", total//len(numbers))
