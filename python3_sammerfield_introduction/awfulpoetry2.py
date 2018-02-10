#!/usr/bin/env python3
import random
count = 0
while True:
    try:
        counts = input ('Введите желаемое количество строк:')
        if not counts:
            counts = 5
        counts = int(counts)
        if counts <= 0:
            print ('введите цифру больше 0')
            continue
    except ValueError as err:
        print ('это не цифра')
    while count < counts:
        article = random.choice (['the', 'his', 'her', 'my'])
        noun = random.choice (['cat', 'dog', 'man', 'woman', 'horse'])
        verb = random.choice (['sang', 'ran', 'jumped', 'swimmed', 'heard'])
        adverb = random.choice (['loudly', 'quietly', 'well', 'badly'])
        structure = random.randint(1, 2)
        if structure < 2:
            print (article, noun, verb, adverb)
        else:
            print (article, noun, verb)
        count += 1
    break