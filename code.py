def addition(num1, num2):
    return num1 + num2

def multiplication(num1, num2):
    return num1 * num2

def subtraction(num1, num2):
    return num1 - num2

def division(num1, num2):
    return num1/num2

def avg(num1, num2):
    return (num1+num2)/2
    
print('''
            Welcome to pycalculator.
            A basic python calculator made by natrix.
            |------------------------------------------|
            |1 - Addition                              |
            |2 - Subtraction                           |
            |3 - Division                              |
            |4 - Multiplication                        |
            |5 - Avarage                               |
            |------------------------------------------|
            ''')
loop = True
while loop:


    user_input = int(input("Select one operator (1, 2, 3, 4, 5, 6) : "))
    numput1 = int(input('Type first number: '))
    numput2 = int(input('Type second number: '))

    if user_input == 1:
        print(numput1, '+', numput2, '=', addition(numput1, numput2))

    elif user_input == 2:
        print(numput1, '-', numput2, '=', subtraction(numput1, numput2))

    elif user_input == 3:
        print(numput1, '÷', numput2, '=', division(numput1, numput2))

    elif user_input == 4:
        print(numput1, '*', numput2, '=', multiplication(numput1, numput2))
    elif user_input == 5:
        print('Avarage of', numput1, ' and ', numput2, ' is ', avg(numput1, numput2))

    else:
        print('Invalid input please select a operator from (1, 2, 3, 4, 5)')
