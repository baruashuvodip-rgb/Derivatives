#include <iostream>
using namespace std;

void test_func(string x) {
    cout<<"Ha! you said "<<x<<"!"<<endl;
}
int main() {
    string x;
    cout<<"Say something"<<endl;
    cin>>x;
    test_func(x);
    return 0;
}