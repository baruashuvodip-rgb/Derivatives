#include <iostream>
#include <cmath>
#include <gsl/gsl_deriv.h>

double f(double x, void *params) {
    return (x- 2.5)*(x- 2.5)*(x- 2.5) + 16;
}

int main() {
    double result, err;
    gsl_function F;
    F.function = &f;
    gsl_deriv_central(&F, 4.0, 1E-6, &result, &err);
    std::cout << "Central derivative result: " << result << " +/- " << err
    << "\n";
    gsl_deriv_forward(&F, 4.0, 1E-6, &result, &err);
    std::cout << "Forward derivative result: " << result << " +/- " << err
    << "\n";
    gsl_deriv_backward(&F, 4.0, 1E-6, &result, &err);
    std::cout << "Backward derivative result: " << result << " +/- " << err
    << "\n";
    return 0;
}