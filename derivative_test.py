from scipy.differentiate import derivative
import math
import finiteDiff as diff

x = float(input("Enter x value:"))

f_choice = int(input("Which function would you like to test?\n1.Polynomial\n2.Trigonometric\n3.Exponential\n4.Logarithmic\n"))

def f(x):
    match f_choice:
        case 1:
            return 49*x**6 + 48*x**5 + 3*x**4 + 39*x*x + 23*x + 35
        case 2:
            return 3*math.sin(10*x - 0.2)
        case 3:
            return 14*math.exp(-(x-3)**2)
        case 4:
            return 5*math.log(x)


def df(x):
    match f_choice:
        case 1:
            return 294*x**5 + 240*x**4 + 12*x**3 + 78*x + 23
        case 2:
            return 30*math.cos(10*x - 0.2)
        case 3:
            return -28*(x-3)*math.exp(-(x-3)**2)
        case 4:
            return 5/x

#def d2f(x):
#    return 1470*x**4 + 960*x**3 + 36*x**2 + 78

#def d3f(x):
#    return 5880*x**3 + 2880*x**2 + 72*x

#def d4f(x):
#    return 17640*x**2 + 5760*x + 72

#def d5f(x):
#    return 35280*x + 5760

#def d6f(x):
#    return 35280

def error(calc, exact):
    error_value = abs((calc-exact))*100/exact
    if(exact==0):
        error_value = 100 
    print("With percentage error", error_value,"%")

deg = int(input("Enter degree of accuracy:"))
h = 10**-deg
n = int(input("Enter order of derivative:"))

if(n<1):
    print("Order Input is Invalid")

elif(n==1):
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
            result = derivative(f,x,order = deg).df
            print("The library function-calculated derivative is", result)

        case _:
            print("Invalid input")

    error(result, df(x))

elif(n==2):
    choice = int(input("How do you want the derivative calculated?\n1. Second Derivative Difference Formula\n"\
                       "2. Forward Difference Recursive Differentiation\n3. Backward Difference Recursive Differentiation"\
                        "\n4. Central Difference Recursive Differentiation\n"))
    match choice:

        case 1:
            result = diff.second(f,x,h)
            print("The second derivative difference formula-calculated derivative is", result)

        case 2:
            result = diff.forwardDiff_recursive(f,x,h,n)
            print("The forward difference recursively calculated derivative is", result)

        case 3:
            result = diff.backwardDiff_recursive(f,x,h,n)
            print("The backward difference recursively calculated derivative is", result)

        case 4:
            result = diff.centralDiff_recursive(f,x,h,n)
            print("The central difference recursively calculated derivative is", result)        

        case _:
            print("Invalid input")

    error(result, diff.centralDiff_recursive(f,x,h,n))

else: # n > 2
    choice = int(input("How do you want the derivative calculated?\n1. Forward Difference Recursive Differentiation\n"\
                       "2. Backward Difference Recursive Differentiation\n3. Central Difference Recursive Differentiation\n"))
    
    match choice:

        case 1:
            result = diff.forwardDiff_recursive(f,x,h,n)
            print("The forward difference recursively calculated derivative is", result)

        case 2:
            result = diff.backwardDiff_recursive(f,x,h,n)
            print("The backward difference recursively calculated derivative is", result)

        case 3:
            result = diff.centralDiff_recursive(f,x,h,n)
            print("The central difference recursively calculated derivative is", result)

        case _:
            print("Invalid input")

    error(result,diff.centralDiff_recursive(f,x,h,n))