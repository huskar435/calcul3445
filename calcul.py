user_input=input()
opertation='Error'
for i in user_input: 
    if i == '+':
        opertation=i
        number_list=user_input.split('+')
    elif i == '-':
        opertation=i
        number_list=user_input.split('-')
    elif i == '*':
        opertation=i
        number_list=user_input.split('*')
    elif i == '/':
        opertation=i
        number_list=user_input.split('/')

def add():
    result=float(number_list[0])
    for g in range(1,len(number_list)):
        result+=float(number_list[g])
    print(result)

def subtract():
    result=float(number_list[0])
    for g in range(1,len(number_list)):
        result-=float(number_list[g])
    print(result)

def multiply():
    result=float(number_list[0])
    for g in range(1,len(number_list)):
        result*=float(number_list[g])
    print(result)

def devide():
    result=float(number_list[0])
    for g in range(1,len(number_list)):
        result/=float(number_list[g])
    print(result)

match opertation:
    case '+':
        add()
    case '-':
        subtract()
    case '*':
        multiply()
    case '/':
        devide()
    case _:
        print(opertation)