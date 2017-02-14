//https://www.hackerrank.com/challenges/queue-using-two-stacks
// g++ Queue_using_two_stacks.cpp -g -std=c++11
// Timeout
#include<stack>
#include<iostream>

int main()
{
    int queries, operation;
    std::stack<int> s1;
    std::stack<int> s2;
    std::cin >> queries;
    
    while(queries)
    {
        std::cin >> operation;
        switch(operation)
        {
            case 1:
                    int v;
                    std::cin >> v;
                    s1.push(v);
                    break;
            case 2:
                    if(s2.empty())
                        while(! s1.empty())
                        {
                            s2.push(s1.top());
                            s1.pop();
                        }
                    s2.pop();
                    break;
            case 3:
            default:
                    if(s2.empty())
                        while(! s1.empty())
                        {
                            s2.push(s1.top());
                            s1.pop();
                        }
                    std::cout << s2.top() << std::endl;
                    break;
        }
    }

    return (0);
}