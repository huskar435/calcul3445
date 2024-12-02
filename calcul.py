


def add(number_list):
    result = float(number_list[0])
    for g in range(1, len(number_list)):
        result += float(number_list[g])
    return result

def subtract(number_list):
    result = float(number_list[0])
    for g in range(1, len(number_list)):
        result -= float(number_list[g])
    return result

def multiply(number_list):
    result = float(number_list[0])
    for g in range(1, len(number_list)):
        result *= float(number_list[g])
    return result

def divide(number_list):
    result = float(number_list[0])
    for g in range(1, len(number_list)):
        result /= float(number_list[g])
    return result

def degree(number_list):
    result = float(number_list[0])
    degree_2 = float(number_list[1])
    for g in range(2, len(number_list)):
        degree_2 *= float(number_list[g])
    return result ** degree_2

def factorial(number_list):
    result = float(number_list[0])


user_input = input("Введите выражение: ")
operation = 'Error'
number_list = []

for i in user_input:
    if i == '+':
        operation = i
        number_list = user_input.split('+')
        break
    elif i == '-':
        operation = i
        number_list = user_input.split('-')
        break
    elif i == '*':
        operation = i
        number_list = user_input.split('*')
        break
    elif i == '/':
        operation = i
        number_list = user_input.split('/')
        break
    elif i == '^':
        operation = i
        number_list = user_input.split('^')
        break
    elif i == '!':
        operation = i
        number_list = user_input.split('!')
        break


if operation == '+':
    print(add(number_list))
elif operation == '-':
    print(subtract(number_list))
elif operation == '*':
    print(multiply(number_list))
elif operation == '/':
    print(divide(number_list))
elif operation == '^':
    print(degree(number_list))
elif operation == '!':
    print(factorial(number_list))
else:
    print("Error")
    

