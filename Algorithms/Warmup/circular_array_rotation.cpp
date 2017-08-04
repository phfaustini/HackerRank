/*https://www.hackerrank.com/challenges/circular-array-rotation*/
/* g++ circular_array_rotation.cpp -std=c++11*/
/*DONE*/
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

int main(){
    int n;
    int k;
    int q;
    cin >> n >> k >> q;
    vector<int> a(n);
    vector<int> b(n);
    
    for(int a_i = 0; a_i < n; a_i++){
       cin >> a[a_i];
    }

    // Rotation
    int newIndex = 0;
    for (int i(0); i < n; i++)
    {
        newIndex = (i + k) % n;
        b[newIndex] = a[i];
    }
        

    for(int a0 = 0; a0 < q; a0++){
        int m;
        cin >> m;
        cout << b[m] << endl;
    }
    return 0;
}
