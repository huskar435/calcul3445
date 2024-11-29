s=input()
opertation='Error'
for i in s: 
    if i == '+':
        opertation=i
        s=s.split('+')
    elif i == '-':
        opertation=i
        s=s.split('-')
    elif i == '*':
        opertation=i
        s=s.split('*')
    elif i == '/':
        opertation=i
        s=s.split('/')   
x=int(s[0])
y=int(s[1])
def add(a,b):
    result=a+b
    print(result)

def subtract(a,b):
    result=a-b
    print(result)

def multyply(a,b):
    result=a*b
    print(result)

def devide(a,b):
    result=a/b
    print(result)

match opertation:
    case '+':
        add(x,y)
    case '-':
        subtract(x,y)
    case '*':
        multyply(x,y)
    case '/':
        devide(x,y)
    case _:
        print(opertation)
        