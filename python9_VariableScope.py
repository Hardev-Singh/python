# Variable Scope
'''
LEGB
Local, Enclosing, Global, Built-in
'''
x = 'global v'

def test():
    x = 'local v'
    print(x)

test()
print(x)

def test1():
    global y
    y = 'local v'
    print(y)

test1()
print(y)

def test1():
    global x
    x = 'local v'
    print(x)

test1()
print(x)


for a in range(2):
    x = 'global {}'.format(a)


def outer():
    # x = 'outer x'
    for b in range(3):
        x = 'outer {}'.format(b)

    def inner():
	    # to define value of x within in enclosing function
	    # nonlocal x     
        # x = 'inner x'
        for c in range(4):
            x = 'inner {}'.format(c)
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)

outer()
print(x)
print(a)