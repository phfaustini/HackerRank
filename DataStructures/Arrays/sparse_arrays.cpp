//https://www.hackerrank.com/challenges/sparse-arrays
//g++ sparse_arrays.cpp -std=c++11
// DONE
#include<iostream>
#include<map>
#include<string>

using namespace std;

int main()
{
    map<string, int> myHash;
    int number_strings;
    cin >> number_strings;
    string word;
    while(number_strings)
    {    
        cin >> word;
        myHash[word] += 1;
        number_strings--;
    }
    int queries, i=0;
    cin >> queries;
    int * output = new int[queries];
    while(queries)
    {
        cin >> word;
        *(output+i) = myHash[word];
        i++;
        queries--;
    }
    for (int j(0); j<i;j++)
        cout << *(output+j) << endl;
}