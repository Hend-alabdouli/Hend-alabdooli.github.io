#include <iostream>

using namespace std;

int main()
{
    float cel,far;
    cout<<"Enter temperature in Celsius:";
    cin>> cel;
    far = ((9.0/5.0)*cel)+ 32;
    cout<< "Temperature in Farenheit:"<<far<<"\n"; 
    return 0;
 }
