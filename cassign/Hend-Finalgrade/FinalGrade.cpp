#include <iostream>

using namespace std;

int main()
{
    float ast, lab, mid, fin, Total;
    cout<<"Enter the mark in assignments (out of 20):";
    cin>> ast;
    while (ast <0 || ast > 20){
        cout<<"Invaild input, please enter again (out of 20):";
        cin>> ast;
    }
    cout<<"Enter the mark of lab (out of 10):";
    cin>> lab;
    while (lab <0 || lab > 10){
        cout<<"Invaild input, please enter again (out of 10):";
        cin>> lab;
    }
    cout<<"Enter the mark of midterm exam (out of 30):";
    cin>> mid;
    while (mid <0 || mid > 30){
        cout<<"Invaild input, please enter again (out of 30):";
        cin>> mid;
    }
    cout<<"Enter the mark of final exam (out of 40):";
    cin>> fin;
    while (fin <0 || fin > 40){
        cout<<"Invaild input, please enter again (out of 40):";
        cin>> fin;
    }
    Total=ast+lab+mid+fin;
    cout<< "Total Score ="<<Total<<"\n";
    if (Total >= 90) {
        cout<< "Grade = A"<<"\n";
    }
    else if (Total<90 && Total>=80 ) {
        cout<< "Grade = B"<<"\n";
    }
    else if (Total<80 && Total>=70 ) {
        cout<< "Grade = C"<<"\n";
    }
    else if (Total<70 && Total>=60 ) {
        cout<< "Grade = D"<<"\n";
    }
    else {
        cout<< "Grade = F"<<"\n";
    }
    
    return 0;
   
}
