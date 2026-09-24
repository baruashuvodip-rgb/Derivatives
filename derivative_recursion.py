import numpy as np

def higher_order_derivative(x, y, n):
    """Compute the n-th derivative numerically."""
    if n == 1:
        return np.gradient(y, x)
    else:
        return np.gradient(higher_order_derivative(x, y, n-1), x)

# Example: 3rd derivative of cos(x)
x = float(input("Enter x: "))
y = np.cos(x)
y3 = higher_order_derivative(x, y, 3)

print(y3)