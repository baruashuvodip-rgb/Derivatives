import finiteDiff as diff

x = float(input("Enter x value:"))

def f(x):
    return 49*x**6 + 48*x**5 + 3*x**4 + 39*x*x + 23*x + 35

def df(x):
    return 294*x**5 + 240*x**4 + 12*x**3 + 78*x + 23

def d2f(x):
    return 1470*x**4 + 960*x**3 + 36*x**2 + 78

def d3f(x):
    return 5880*x**3 + 2880*x**2 + 72*x

def d4f(x):
    return 17640*x**2 + 5760*x + 72

def d5f(x):
    return 35280*x + 5760

def d6f(x):
    return 35280

deg = int(input("Enter degree of accuracy:"))
h = 10**-deg
n = int(input("Enter order of derivative:"))

choice = int(input("How do you want the derivative calculated?\n1. Direct calculation (""by hand"")" \
        "\n2. Forward difference\n3. Backward Difference\n4. Central Difference\n5. Extrapolated Difference" \
        "\n6. Recursive Differentiation\n"))

match choice:

    case 1:
        match n:
            case 1:
                print("The directly (by-hand) calculated derivative is:", df(x))
            case 2:
                print("The directly (by-hand) calculated derivative is:", d2f(x))
            case 3:
                print("The directly (by-hand) calculated derivative is:", d3f(x))
            case 4:
                print("The directly (by-hand) calculated derivative is:", d4f(x))
            case 5:
                print("The directly (by-hand) calculated derivative is:", d5f(x))
            case 6:
                print("The directly (by-hand) calculated derivative is:", d6f(x))
            case _:
                print("The directly (by-hand) calculated derivative is: 0")
                
    case 2:
        print("The forward difference derivative is", diff.forward(f,x,h))

    case 3:
        print("The backward difference derivative is", diff.backward(f,x,h))

    case 4:
        print("The central difference derivative is", diff.central(f,x,h))

    case 5:
        print("The extrapolated difference derivative is", diff.extrapolated(f,x,h))

    case 6:
        print("The recursively calculated derivative is", diff.centralDiff_recursive(f,x,h,n))

    case _:
        print("Invalid input")