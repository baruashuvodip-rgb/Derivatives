from scipy.differentiate import derivative
import finiteDiff as diff

x = float(input("Enter x value:"))

def f(x):
    return 49*x**6 + 48*x**5 + 3*x**4 + 39*x*x + 23*x + 35

def df(x):
    return 294*x**5 + 240*x**4 + 12*x**3 + 78*x + 23

def d2f(x):
    return 1470*x**4 + 960*x**3 + 36*x**2 + 78

def error(calc, exact):
    print("With percentage error", (calc-exact)*100/exact,"%")

deg = int(input("Enter degree of accuracy:"))
h = 10**-deg
n = int(input("Enter order of derivative:"))

if(n==1):
    choice = int(input("How do you want the derivative calculated?\n1. Direct calculation (""by hand"")" \
        "\n2. Forward difference\n3. Backward Difference\n4. Central Difference\n5. Extrapolated Difference" \
        "\n6. Recursive Differentiation\n7. Library Function\n"))

    match choice:

        case 1:
            result = df(x)
            print("The directly (by-hand) calculated derivative is:", result)
                    
        case 2:
            result = diff.forward(f,x,h)
            print("The forward difference derivative is", result)
            
        case 3:
            result = diff.backward(f,x,h)
            print("The backward difference derivative is", result)

        case 4:
            result = diff.central(f,x,h)
            print("The central difference derivative is", result)

        case 5:
            result = diff.extrapolated(f,x,h)
            print("The extrapolated difference derivative is", result)

        case 6:
            result = diff.centralDiff_recursive(f,x,h,n)
            print("The recursively calculated derivative is", result)

        case 7:
            result = derivative(f,x,order = deg)
            print("The library function-calculated derivative is", result)

        case _:
            print("Invalid input")

    error(result, df(x))

elif(n==2):
    choice = int(input("How do you want the derivative calculated?\n1. Direct Calculation(""by-hand"")\n"\
                       "2. Second Derivative Difference Formula\n3. Recursive Differentiation\n"))
    match choice:

        case 1:
            result = d2f(x)
            print("The directly (by-hand) calculated derivative is:", result)
                    
        case 2:
            result = diff.second(f,x,h)
            print("The second derivative difference formula-calculated derivative is", result)

        case 3:
            result = diff.centralDiff_recursive(f,x,h,n)
            print("The recursively calculated derivative is", result)

        case _:
            print("Invalid input")

    error(result, d2f(x))

else: # n > 2
    choice = int(input("How do you want the derivative calculated?\n1. Recursive Differentiation\n"))
    
    match choice:

        case 1:
            result = diff.centralDiff_recursive(f,x,h,n)
            print("The recursively calculated derivative is", result)

        case _:
            print("Invalid input")

    error(result, d2f(x))
