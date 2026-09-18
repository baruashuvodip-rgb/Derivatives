#include <iostream>
#include <cmath>
using namespace std;

double x_function (double x) {
    return 3*x*x*x -26;
}

void forward (double x, double h, double (*func)(double)){
    cout << "The forward difference derivative is " << (func(x+h) - func(x))/h <<endl;
}

void backward (double x, double h, double (*func)(double)){
    cout << "The backward difference derivative is " << (func(x) - func(x-h))/h <<endl;
}

void central (double x, double h, double (*func)(double)){
    cout << "The central difference derivative is " << ((func(x+h/2) - func(x-h/2))/h)<<endl;
}

void extrapolated(double x, double h, double (*func)(double)){
    double result = (8*func(x+h/4)-8*func(x-h/4)-func(x+h/2)+func(x-h/2))/(3*h);
    cout<< "The extrapolated difference derivative is " << result <<endl;
}

void second (double x, double h, double (*func)(double)){
    double result = 4*(func(x + h/2) + func(x- h/2)- 2*func(x))/(h*h);
    cout << "The second derivative is " <<result<<endl;
}

int main() {
    double x, h;
    int deg;
    cout << "Enter x value: ";
    cin >> x;
    h = 0.0001;

    forward(x,h,x_function);
    backward(x,h,x_function);
    central(x,h,x_function);
    extrapolated(x,h,x_function);
    second(x,h,x_function);
    return 0;
}