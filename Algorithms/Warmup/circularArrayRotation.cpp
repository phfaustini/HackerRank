/*https://www.hackerrank.com/challenges/circular-array-rotation*/
/* g++ circularArrayRotation.cpp -std=c++11*/
/*Timeout happens*/
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

class myArray{
    private:
        vector<int> arr;
    public:
        void addElement(int v)
        {
            arr.push_back(v);
        }

        vector<int> getArr()
        {
            return arr;
        }

        void rotateRight()
        {
            int last = arr[0], current;
            for (int i(1); i < arr.size(); i++)
            {
                current = arr[i];
                arr[i] = last;
                last = current;                 
            }
            arr[0] = last;
        }

        int getElement(int index)
        {
            return arr[index];
        }
};

int main(){
    int n;
    int k;
    int q;
    int temp;
    cin >> n >> k >> q;
    myArray a;
    
    for(int a_i = 0; a_i < n; a_i++){
       cin >> temp;
       a.addElement(temp);
    }

    for (int i(0); i < k; i++)
        a.rotateRight();

    for(int a0 = 0; a0 < q; a0++){
        int m;
        cin >> m;
        cout << a.getElement(m) << endl;
    }
    return 0;
}
