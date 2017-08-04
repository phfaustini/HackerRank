// https://www.hackerrank.com/challenges/caesar-cipher-1
// g++ caesar_cipher.cpp -std=c++11
// DONE
#include<iostream>
#include<string>
using namespace std;
int main()
{
    int length;
    string s;
    int key;
    cin >> length >> s >> key;
    key = (key % 26);
    if (key % 26 == 0)
        cout << s << endl;
    else
    {    
        for (int i(0); i< s.size(); i++)
        {
            if( s[i] >= 65 && s[i] <=90)
            {
                s[i] = (s[i] + key) % 91;
                if(s[i] < 65) s[i] += 65;
            }
            else if (s[i]>=97 && s[i] <=122)
            {
                s[i] = (s[i] + key) % 123;
                if(s[i] < 97) s[i] += 97;
            }
        }
        cout << s << endl;
    }
    return (0);
}