def f(x):
    return 3*x*x*x - 26

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

x = float(input("Enter x value: "))
acc = int(input("Enter degree of accuracy: "))
h = 10**-acc
print(h)

print("The forward difference derivative is", forward(f,x,h))
print("The backward difference derivative is", backward(f,x,h))
print("The central difference derivative is", central(f,x,h))
print("The extrapolated difference derivative is", extrapolated(f,x,h))
print("The second derivative is", second(f,x,h))
