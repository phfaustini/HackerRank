//https://www.hackerrank.com/challenges/jesse-and-cookies
//g++ -g jesse_and_cookies.cpp -std=c++11
// Timeout
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    vector<int> cookies;
    while(n)
    {
        int c;
        cin >> c;
        cookies.push_back(c);
        n--;
    }

    sort(cookies.begin(), cookies.end());

    bool stop = false;
    int operations = 0;
    while(! stop)
    {
        if(cookies[0] < k)
        {
            if(cookies.size() > 1)
            {
                int temp = cookies[0] + 2*cookies[1];
                cookies.erase(cookies.begin(), cookies.begin()+2);
                cookies.push_back(temp);
                sort(cookies.begin(), cookies.end());
                operations++;
            }
            else
            {
                stop = true;
                operations = -1;
            }
        }
        else stop = true;
    }
    cout << operations << endl;
    return(0);
}