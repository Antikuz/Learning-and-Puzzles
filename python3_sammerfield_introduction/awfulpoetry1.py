#!/usr/bin/env python3
import random
count = 0
while count < 5:
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