import random
a = None  # a is start number
b = None  # b is end number
# a and b are so that if the try code doesnt work we dont need to check if it works or if the start and end numbers are there
print('''
Hello!
This is a game in which you try to guess a number which a computer randumly choses 
First you will need to enter to numbers and than the computer will chose a number between those two numbers ''')
while True:
    try:
        a = int(input('Here you\'ll enter the first number:  '))
        b = int(input('and here you will enter the second number:  '))
        break
    except ValueError or IndexError:
        print('you need to enter a number')
        continue

while a > b:
    try:
        a = int(input('the first number that you have entered was higher than the second please enter a number lower than the second one:  '))
        break
    except ValueError or IndexError:
        print('you need to enter a number')
        continue
print('great now the program will chose a random number')

startnum = random.randint(a, b)
print('great now we are all set')
c = None  # its set to none so that we can later change it

c = int(input('please enter a number that you think is right:  '))


while c != startnum:
    try:
        if c < startnum + 10 and c > startnum:
            c = int(
                input('you guesssed a number that is greater and close to the right number but it wasnt right please try agian:  '))
        elif c > startnum - 10 and c < startnum:
            c = int(
                input('you guesssed a number that is lower and close to the right number but it wasnt right please try agian:  '))
        elif c > startnum:
            c = int(input(
                'you have guessed a numbere greater than the right number please enter a new number:  '))
        else:
            c = int(
                input('you guessed a number lower than the right number please try agian:  '))
    except ValueError or IndexError:
        print('Please enter a number')
        continue

if c == startnum:
    print('great you have guesssed the right number')
