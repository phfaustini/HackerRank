//https://www.hackerrank.com/challenges/queue-using-two-stacks
// g++ Queue_using_two_stacks.cpp -g -std=c++11
// Timeout
#include<stack>
#include<iostream>

typedef struct
{
    int value;
    int first;
}SQ;

int main()
{
    int queries, operation;
    std::stack<SQ> s1;
    std::stack<SQ> s2;
    std::cin >> queries;
    
    while(queries)
    {
        std::cin >> operation;
        switch(operation)
        {
            case 1:
                    SQ e;
                    int v;
                    std::cin >> v;
                    e.value = v;
                    if(s1.empty())
                        e.first = e.value;
                    else
                        e.first = s1.top().first;
                    s1.push(e);
                    break;
            case 2:
                    if(s2.empty())
                        while(! s1.empty())
                        {
                            s2.push(s1.top());
                            s1.pop();
                        }
                    s2.pop();
                    
                    if(! s2.empty())
                        s2.top().first = s2.top().value;
                    break;
            case 3:
            default:
                    if(s2.empty())
                        std::cout << s1.top().first << std::endl;
                    else
                        std::cout << s2.top().first << std::endl;
                    break;
        }
    }

    return (0);
}