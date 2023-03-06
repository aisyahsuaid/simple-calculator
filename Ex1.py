# Menu driven calculator for two numbers

# Addition
def addition(x, y):
    return x + y

# Substraction
def sub(x, y):
    return x - y

# Multiplication
def mult(x, y):
    return x * y

# Division
def div(x, y):
    return x / y

# Calculator interface

print('Welcome to my simple calculator program :D')
print('1. Addition')
print('2. Substraction')
print('3. Multiplication')
print('4. Division')
print('5. Quit program')

#User input 
while True:
    choice1 = int(input('Please choose your desired operation: '))

    if choice1 == 1:
        x = int(input('Enter your first number: '))
        y = int(input('Enter your second number: '))
        print(addition(x, y))
    elif choice1 == 2:
        x = int(input('Enter your first number: '))
        y = int(input('Enter your second number: '))
        print(sub(x, y))
    elif choice1 == 3:
        x = int(input('Enter your first number: '))
        y = int(input('Enter your second number: '))
        print(mult(x, y))
    elif choice1 == 4:
        x = int(input('Enter your first number: '))
        y = int(input('Enter your second number: '))
        print(div(x, y))
    elif choice1 == 5:
        quit()
    else: 
        print('Invalid input')

