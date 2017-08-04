// g++ truck_tour.cpp -std=c++11 -g
// https://www.hackerrank.com/challenges/truck-tour
// DONE
#include<iostream>
#include<vector>
using namespace std;

typedef struct pp
{
    int petrol;
    int distance;
} petrol_pump;

int main()
{
    int n;
    cin >> n;
    vector<petrol_pump> p;
    
    for(int i(0); i< n;i++)
    {
        petrol_pump temp;
        cin >> temp.petrol;
        cin >> temp.distance;
        p.push_back(temp);
    }

    int minimum_index = -1;
    for(int i(n-1); i>=0; i--)
    {
        int petrols = n;
        int current = i;
        int fuel = 0;
        bool stop = false;
        while(petrols)
        {
            fuel += p[current].petrol;
            if(p[current].distance > fuel)
            {
                stop = true;
                break;
            }
            else
            { 
                fuel -= p[current].distance;
                current = (current + 1) % n;
                petrols--;
                
            }
        }
        if(! stop)
            minimum_index = i;
    }

    cout << minimum_index << endl;

    return (0);
}