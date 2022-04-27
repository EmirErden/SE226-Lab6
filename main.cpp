#include <iostream>
using namespace std;

float product = 1.0;

float capital_pi(float number){
    if (number >= 1){
        product = (number/(number+2))-10 * capital_pi(number-1);
    }
    return product;
}

int a = 1;

float capital_pi() {
    float user_number;
    if (a == 1) {
        cout << "Please enter a number for calculation: ";
        cin >> user_number;
    } else {

        user_number = user_number - 1;

        if (user_number >= 1) {
            product = (user_number / (user_number + 2)) - 10 * capital_pi();
            a = 3;
        }
    }
    return product;
}

int main(){
    float user_number;
    cout << "Please enter a number for calculation: ";
    cin >> user_number;
    cout << capital_pi(user_number) << endl;

    cout << capital_pi();
}

