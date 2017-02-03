//https://www.hackerrank.com/challenges/maximum-element
// g++ maximum_element.cpp -std=c++11 -g

#include<iostream>
#include<stack>
using namespace std;
int main()
{
    int q, popIgnore = 0, biggest = 0;
    cin >> q;
    stack<int> myStack;
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
                        myStack.push(n);
                        biggest = n;
                    }
                    else if (n > myStack.top())
                    {
                        myStack.push(n);
                        biggest = n;
                    }
                    else
                    {
                        popIgnore++;
                        biggest = 0;
                    }
                    break;
            case 2: // Pop element
                    if(!popIgnore || biggest)
                        myStack.pop();
                    else 
                        popIgnore--;
                    break;
            case 3: // Print maximum element
                    cout << myStack.top() << endl;
                    break;
        }
    }
    return (0);
}