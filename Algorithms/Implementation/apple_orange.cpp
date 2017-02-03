//https://www.hackerrank.com/challenges/apple-and-orange
// g++ apple_orange.cpp -std=c++11
// DONE
#include<iostream>
#include<vector>

using namespace std;


int main(){
    int s; // start house
    int t; // end house
    cin >> s >> t;
    int a; // apple location
    int b; // orange location
    cin >> a >> b;
    int m; // apples falling
    int n; // oranges falling
    cin >> m >> n;
    vector<int> apple(m);
    int apples = 0;
    int oranges = 0; 

    for(int apple_i = 0; apple_i < m; apple_i++){
       cin >> apple[apple_i];
       apple[apple_i] += a;
       if (apple[apple_i] >= s && apple[apple_i] <= t)
            apples++; 
    }

    vector<int> orange(n);
    for(int orange_i = 0; orange_i < n; orange_i++){
       cin >> orange[orange_i];
       orange[orange_i] += b;
       if(orange[orange_i] >= s && orange[orange_i] <= t)
            oranges++;
    }

    cout << apples << endl << oranges << endl;
    return 0;
}
