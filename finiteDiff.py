def f(x):
    return 49*x**6 + 48*x**5 + 3*x**4 + 39*x*x + 23*x + 35

def df(x):
    return 294*x**5 + 240*x**4 + 12*x**3 + 78*x + 23

def d2f(x):
    return 1470*x**4 + 960*x**3 + 36*x**2 + 78

def forward (f,x,h):
    return (f(x+h)-f(x))/h

def backward (f,x,h):
    return (f(x)-f(x-h))/h

def central (f,x,h):
    return (f(x+h/2)-f(x-h/2))/h;

def extrapolated (f,x,h):
    return (8*f(x+h/4)-8*f(x-h/4)-f(x+h/2)+f(x-h/2))/(3*h)

def second (f,x,h):
    return 4*(f(x + h/2) + f(x- h/2)- 2*f(x))/(h*h)
 
def centralDiff_recursive(f, x, h, n=1):
    result = 0.0
    if (n > 1):
        h = h**(1/n)
        result = (centralDiff_recursive(f, x + h/2, h, n-1)- centralDiff_recursive(f, x- h/2, h, n-1))/h
    else:
        result = (f(x + h/2)- f(x- h/2))/h
    return result

#x = float(input("Enter x value: "))
#acc = int(input("Enter degree of accuracy: "))
#h = 10**-acc
#print(h)

#print("The forward difference derivative is", forward(f,x,h))
#print("The backward difference derivative is", backward(f,x,h))
#print("The central difference derivative is", central(f,x,h))
#print("The extrapolated difference derivative is", extrapolated(f,x,h))
#print("The second derivative is", second(f,x,h))
#print("The derivative calculated recursively is", centralDiff_recursive(f,x,h,acc))
