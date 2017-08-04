// https://www.hackerrank.com/challenges/pacman-dfs
// g++ pacman_dfs.cpp -std=c++1y -g

#include <iostream>
#include <vector>
#include <stack>
#include <set>

#define FORBIDDEN '%'
#define VALID '-'

typedef struct 
{
    int r;
    int c;
}coordinates;

// UP:    [i-1] [j]
// LEFT   [i] [j-1]
// RIGHT  [i] [j+1]
// DOWN   [i+1] [j]
// Print the number of nodes explored ( a node is marked explored only when the node is popped out of the stack ) 


void dfs( int r, int c, int pacman_r, int pacman_c, int food_r, int food_c, std::vector <std::string> grid)
{
	std::vector<coordinates> to_print;
	std::set<coordinates> visited; std::set<coordinates>::iterator it;
	std::stack<coordinates> mystack;

    coordinates init;
    init.r = pacman_r;
    init.c = pacman_c;

    mystack.push(init);

    while(! mystack.empty())
    {
        coordinates v = mystack.top();
        to_print.push_back(v);
        if (v.r = food_r && v.c == food_c)
            break;
        mystack.pop();
        

        it = visited.find(v);
        

    }
    
}


int main(void)
{
    int r,c, pacman_r, pacman_c, food_r, food_c;

    std::cin >> pacman_r >> pacman_c;
    std::cin >> food_r >> food_c;
    std::cin >> r >> c;

    std::vector<std::string> grid;

    for(int i=0; i<r; i++)
    {
    	std::string s; std::cin >> s;
    	grid.push_back(s);
    }

    dfs( r, c, pacman_r, pacman_c, food_r, food_c, grid);

    return 0;
}

