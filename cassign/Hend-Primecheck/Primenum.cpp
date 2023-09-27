
#include <iostream>

using namespace std;

int main()
{
    int r,n,num;
    cout<<"Enter an integer:";
    cin>> num;
    n=2;
    r=1;
    while (n!=num){
        if (num % n==0){
            r=0;
            break;
       }
       n=n+1;
    }
    if (r==1){
        cout<<num<<" is a prime number";
    }
    else{
        cout<<num<<" is not a prime number";
    }
   
    
    return 0;
   
}
