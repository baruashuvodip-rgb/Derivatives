#include <iostream>
using namespace std;

// Callback function
int square(int x) {
    return x * x;
}

// Function that takes another function as parameter
void process(int value, int (*func)(int)) {
    cout << "Result: " << func(value);
}

int main() {
    process(5, square);   // Passing function as argument
    return 0;
}