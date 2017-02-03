//https://www.hackerrank.com/challenges/game-of-thrones
// g++ gameofthronesI.cpp -std=c++11
// DONE
#include<iostream>
#include<string>

using namespace std;

int main()
{

    string word;
    cin >> word;
    int * characters = new int[26];
    for(int i(0); i<26; i++) characters[i]=0;
    int odd = 0;

    for (int i(0); i<word.size(); i++)
    {
        characters[ (word[i] - 97) ]++;
    }

    for(int i(0); i<26; i++)
    {
        if(characters[i] % 2 > 0)
        {
            odd++;
        }
    }

    if(odd > 1)
        cout << "NO" << endl;
    else cout << "YES" << endl;

    return (0);
}