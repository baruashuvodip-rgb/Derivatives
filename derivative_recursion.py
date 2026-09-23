from scipy.differentiate import derivative

def centralDiff(f, x, h, n=1):
    result = 0.0
    if (n > 1):
        h = h**(1/n)
        result = (centralDiff(f, x + h/2, h, n-1)- centralDiff(f, x- h/2, h, n-1))/h
    else:
        result = (f(x + h/2)- f(x- h/2))/h
    return result

x = float(input("Enter x: "))

def f(x):
    return 3*x**2 - 26


h = 0.0001

order_num = int(input("Enter order of derivative: "))


print("Our Result =", centralDiff(f,x,h,order_num))
#print("Library function Result =", derivative(f,x,order = 4))
library_result = derivative(f,x, order = 2).df

print(library_result)