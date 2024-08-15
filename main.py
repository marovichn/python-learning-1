#import sys
#import random

#sys.argv

#random_number = random.randint(1, 10)

#while True:
#    try:
#        guess = int(input('guess a number 1~10:'))
#        if 0 < guess < 11:
#            if guess == random_number:
#                print("congrats you are genius")
#            else:
#                print("not true")
#                continue
#            break
#        else:
#            print('hey bozo, I said 1~10')
#   except ValueError:\
#        print('please enter a number')
#        continue


#import pyjokes

#while True:
#    inputs = input("press key")
#    if inputs:
#        joke = pyjokes.get_joke("en", "neutral")
#        print(joke)
#        continue



#from collections import Counter, defaultdict, OrderedDict

#sentence = "Nikolaaaaa"
#li = [1, 2, 3, 4, 5, 6, 7]
#print(Counter(sentence))

from translate import Translator

translator = Translator(to_lang="en", from_lang="es")
try:
    with open('test.txt', mode="r") as file:
        text = file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print("Not found")
    raise err




