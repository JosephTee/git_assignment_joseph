def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    print(min(diff1, diff2, diff3))
    pass   

#a, b,c = least_difference(1, 10, 100), least_difference(1, 10, 10), least_difference(5, 6, 7)
#print(a)
#print(b)
#print(c)
#print(a+b+c)


def f(x):
    return 12* x

ans = f(10)
y=10
print("The initial value of y is ", y)
print()
def call(f, arg):
    global y
    y=arg
    #return f(arg)
print("The second value of y is ", y)
call(f, 5)
print(f"The value of y is {y}")
print(call(f,5))
m= call(f, 6)
print(m)
y=12
print(f"After calling with arg 6, the value of y is {y}")