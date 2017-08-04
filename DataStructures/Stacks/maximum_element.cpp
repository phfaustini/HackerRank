//https://www.hackerrank.com/challenges/maximum-element
// g++ maximum_element.cpp -std=c++11 -g

#include<iostream>
#include<stack>
using namespace std;


typedef struct
{
    int value;
    int maxSoFar;
}
STACK;

int main()
{
    int q;
    cin >> q;
    stack<STACK> myStack;
    while(q)
    {
        q--;
        int operation;
        cin >> operation;
        switch(operation)
        {
            case 1: // Push element
                    int n;
                    cin >> n;
                    if(myStack.empty())
                    {
                        STACK s;
                        s.value = n;
                        s.maxSoFar = n;
                        myStack.push(s);
                    }
                    else if(n >= myStack.top().maxSoFar)
                    {
                        STACK s;
                        s.value = n;
                        s.maxSoFar = n;
                        myStack.push(s);
                    }
                    else
                    {
                        STACK s;
                        s.value = n;
                        s.maxSoFar = myStack.top().maxSoFar;
                        myStack.push(s);
                    }
                    break;
            case 2: // Pop element
                    if(! myStack.empty())
                        myStack.pop();
                    break;
            case 3: // Print maximum element
                    cout << myStack.top().maxSoFar << endl;
                    break;
        }
    }
    return (0);
}