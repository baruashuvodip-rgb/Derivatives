def centralDiff(f, x, h, n=1):
    result = 0.0
    if (n > 1):
        h = h**(1/n)
        result = (centralDiff(f, x + h/2, h, n-1)- centralDiff(f, x- h/2, h, n-1))/h
    else:
        result = (f(x + h/2)- f(x- h/2))/h
    return result