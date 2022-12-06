a = None
b = None
c = None
while True:
    try:
        a = int(input('''
1: additon
2: multiply
3: devision
4: subtraction
5: to the power
please enter a number of an action that you want:  '''))
    except ValueError or IndexError:
        print("please enter a number")
        continue
    finally:
        break

while True:
    try:
        b = int(input('please enter the first number:  '))
    except ValueError or IndexError:
        print("please enter a number")
        continue
    finally:
        break

while True:
    try:
        c = int(input('please enter the second number:  '))
    except ValueError or IndexError:
        print("please enter a number")
        continue
    finally:
        break

if a == 1:
    print('here is your number: ', b + c)
elif a == 2:
    print('here is your number: ', b * c)
elif a == 3:
    print('here is your number: ', c / b)
elif a == 4:
    print('here is your number: ', b - c)
elif a == 5:
    print('here is your number: ', b**c)
