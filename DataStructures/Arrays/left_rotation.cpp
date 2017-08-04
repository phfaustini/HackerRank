// https://www.hackerrank.com/challenges/array-left-rotation
//g++ -std=c++11 left_rotation.cpp
// DONE
#include<iostream>

using namespace std;

int main()
{
    int size, rotations;
    cin >> size >> rotations;
    int * array = new int[size];
    int * aux = new int[size];
    for(int i(0); i<size; i++)
        cin >> *(array + i);
    
    rotations %= size;
    
    for(int i(0); i < size; i++)
    {
        int newIndex = i - rotations;
        if(newIndex < 0) newIndex += size;
        aux[ newIndex ] = array[i];
    }

    for(int i(0); i < size; i++)
    {
        cout << aux[i] << " ";
    }
    cout << endl;

    return (0);
}