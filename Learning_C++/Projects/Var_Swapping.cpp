#include <iostream>

using namspaces std;

int main() {
    int a = 1;
    int b = 2;
    int c = a;
    a = b;
    b = c;
    
    cout << a;

    return 0;
}