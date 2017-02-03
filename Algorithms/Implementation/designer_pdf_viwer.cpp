//https://www.hackerrank.com/challenges/designer-pdf-viewer 
// g++ -std=c++11 designer_pdf_viwer.cpp
// DONE
#include<iostream>
#include<string>
using namespace std;

int main()
{
    string word;
    int * alphabet = new int[26];
    int area = 0, tallest = -1;
    for(int i(0); i<26;i++)
        cin >> *(alphabet + i);
    cin >> word;
    
    for (int i(0); i < word.size(); i++)
    {
        if( alphabet[ int(word[i])-97 ] > tallest) 
            tallest = alphabet[ int(word[i])-97 ];
    }        

    cout << tallest * word.size() << endl;

    return (0);
}