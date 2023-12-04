def myfunc():
    print('Hello World')

def myfunc(name):
    print('Hello {}'.format(name))

def myfunc(x):
    if x == True:
        return 'Hello'
    elif x == False:
        return 'Goodbye'

def myfunc(x,y,z):
    if z:
        return x
    else:
        return y

def myfunc(a,b):
    print(a+b)


def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

def is_greater(x,y):
    return x>y

def myfunc(*args):
    return sum(args)

def myfunc(*args):
    out = []
    for num in args:
        if num%2==0:
            out.append(num)
    return out

def myfunc(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)
































































