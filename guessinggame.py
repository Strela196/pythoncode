import sys
import random
a = None  # a is start number
b = None  # b is end number
# a and b are so that if the try code doesnt work we dont need to check if it works or if the start and end numbers are there
while True:
    try:
        try:  # checks if you have enterd any numbers
            # int is so that the number given gets converted from str to int
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            print(a, b)
        except IndexError:  # if you didnt it tells you to
            a = int(input('please re-enter a real start number:'))
            b = int(input('please re-enter a real end number: '))
        except ValueError:
            a = int(
                input('i didnt think you didnt know what a number pleasseee enter a  start number:'))
            b = int(input('so enter an end number: '))
    except IndexError:
        a = int(input('damn you suck enter a start number: '))
        b = int(input('and another number enter a start number: '))
    except ValueError:
        a = int(input(
            'really huh really whyyyy are you doing this pleasseeeeee entere a start number:'))
        b = int(input('and ofc enter an end number: '))
    finally:
        break


startnum = random.randint(a, b)
print(startnum)
c = None  # its set to none so that we can later change it

c = int(input('please enter a number that you think is right:  '))

while c != startnum:
    try:
        if c < startnum + 10 and c > startnum:
            c = int(
                input('you guesssed close but it wasnt right please try agian:  '))
        elif c > startnum - 10 and c < startnum:
            c = int(
                input('you guesssed close but it wasnt right please try agian:  '))
        else:
            c = int(input('you guessed the wrong number please try agian:  '))
    except ValueError or IndexError:
        print('Please enter a number')
        continue

if c == startnum:
    print('great you have guesssed the right number')
