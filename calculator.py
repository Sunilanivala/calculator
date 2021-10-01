def addition():
    total = 0
    count = 0
    try:
        value = float(input('Enter a number or Press Enter to exit : '))
        while len(str(value)) > 0:
            total = total + float(value)
            count = count + 1
            value = input('Enter another number or Press Enter to exit : ')
        return f'Sum is {total} \nTotal numbers entered are {count}'
    except Exception as error:
        return error

def subtraction():
    total = 0
    count = 0
    try:
        value = float(input('Enter a number or Press Enter to exit : '))
        while len(str(value)) > 0:
            value = float(value)
            if total == 0 and count == 0:
                total = value
            else:
                total =   total - value
            count = count + 1
            value = input('Enter another number or Press Enter to exit : ')
        return f'Subtracted value is {total} \nTotal numbers entered are {count}'
    except ValueError as error:
        return error

def multiplication():
    total = 0
    count = 0
    try:
        value = float(input('Enter a number or Press Enter to exit : '))
        while len(str(value)) > 0:
            value = float(value)
            if total == 0 and count == 0:
                total =  value
            else:
                total = total * value
            count = count + 1
            value = input('Enter another number or Press Enter to exit : ')
        return f'Multiplicate the  value is {total} \nTotal numbers entered are {count}'
    except Exception as e:
        return e

def division():
    total = 0
    count = 0
    try:
        value = float(input('Enter a number or Press Enter to exit : '))
        while len(str(value)) > 0:
            value = float(value)
            if total == 0 and count == 0:
                total = total
            else:
                total = total / value
            count = count + 1
            value = input('Enter another number or Press Enter to exit : ')
        return f'Division of value is {total} \n Total number is entered are {count}'
    except Exception as e:
        return e

def average():
    total = 0
    count = 0
    try:
        value = float(input('Enter a number or Press Enter to exit : '))
        while len(str(value)) > 0:
            value  = float(value)
            total = total + value
            count = count + 1
            value = input('Enter another number or Press Enter to exit : ')
        avg = total / count
        return f'Average of value is {round(avg,2)}\n Total numer entered are {count}'
    except ValueError as e:
        return e

while True:
    print('\n')
    print("Let's build a Calculator!")
    print('   Choose an operation: ')
    print('      add --> Addition')
    print('      sub --> Subtraction')
    print('      mul --> Multiplication')
    print('      div --> Division')
    print('      avg --> Average')
    print('      Q -->   Exit')
    print('\n')
    choice = input("What's your choice : ")

    if choice == 'Q' or choice == 'q':
        break
    elif choice == 'add':
        print(addition())
        print()
        flag = input('Do you want to continue (Y/N): ')
        if flag == 'N':
            break
    elif choice == 'sub':
        print(subtraction())
        print()
        flag = input('Do you want to continue (Y/N): ')
        if flag == 'N':
            break
    elif choice == 'mul':
        print(multiplication())
        print()
        flag = input('Do you want to continue (Y/N): ')
        if flag == 'N':
            break
    elif choice == 'div':
        print(division())
        print()
        flag =  input('Do you want to continue (Y/N): ')
        if flag == 'N':
            break
    elif choice == 'avg':
        print(average())
        print()
        flag =  input('Do you want to continue (Y/N): ')
    if flag == 'N':
        break
