//g++ down_to_zero.cpp -g -std=c++11
//https://www.hackerrank.com/challenges/down-to-zero-ii
// Unfinished
#include<iostream>
#include<map>
using namespace std;

int max_d(int n)
{
    if(n<=1) return n;

    int a = n-1, b=2;
    while(a*b != n)
    {
        a--;
        if(a == 0)
        {
            a = n-1;
            b++;
        }
    }
    if (a >= b)
        return (a);
    return (b);
}

int main()
{
    map<int, int> pre_max;
    map<int, int> moves;
    int queries, q;
    cin >> queries;
    while(queries)
    {
        cin >> q;
        int backup = q;
        int m = 0;
        while(q)
        {
            if(moves.count(q) == 0)
            {
                if(pre_max.count(q) == 0)
                {
                    int temp = max_d(q);
                    if(temp == 1 || temp == q) // Prime number
                    {
                        pre_max[q] = q-1;
                        q--;
                    }
                    else // Not prime, apply max_d
                    {
                        pre_max[q] = temp;
                        q = temp;
                    }
                }
                else
                {
                    q = pre_max[q];
                    return(0);
                }
                m++;
            }
            else
            {
                m += moves.count(q);
                q = pre_max[q];
                break;
            }
        }
        moves[backup] = m;
        cout << m << endl;
        queries--;
    }
    return (0);
}
