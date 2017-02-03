//https://www.hackerrank.com/challenges/alternating-characters
// g++ alternating_characters.cpp -std=c++11
// DONE
#include<iostream>
#include<string>
using namespace std;
int main()
{
    int tests;
    string word;
    cin >> tests;
    int * vector = new int[tests];
    int j = 0;
    while(tests)
    {
        cin >> word;
        int removals = 0;
        for(int i(1); i< word.size(); i++)
        {
            if(word[i] == word[i-1])
                removals++;
        }
        tests--;
        vector[j] = removals; j++;
    }

    for(int i(0); i<j;i++)
        cout << vector[i] << endl;
    return (0);
}