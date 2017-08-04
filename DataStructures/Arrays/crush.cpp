//g++ crush.cpp -g -std=c++11
//https://www.hackerrank.com/challenges/crush
// Timeout
#include <iostream>
using namespace std;


int main() 
{
    long n, m, max = 0;
    cin >> n;
    cin >> m;
    long * v = new long[n];
    while(m)
    {
        long a, b, k;
        cin >> a >> b >> k;
        for(long i(a-1); i<b; i++)
        {
            v[i]+=k;
            if(v[i] > max)
                max = v[i];
        }
        m--;
    }
    cout << max << endl;

    return 0;
}
