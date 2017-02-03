//https://www.hackerrank.com/challenges/mini-max-sum
// g++ minimax.cpp -std=c++11
// DONE
#include<vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    vector<long int> myVector(5);
    cin >> myVector[0] >> myVector[1] >> myVector[2] >> myVector[3] >> myVector[4];
    sort(myVector.begin(), myVector.end());
    long int mininum = myVector[0] + myVector[1] + myVector[2] + myVector[3];
    long int maximum = mininum - myVector[0] + myVector[4];
    cout << mininum << " " << maximum << endl;

    return 0;
}
