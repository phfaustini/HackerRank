//https://www.hackerrank.com/challenges/richie-rich
// g++ richie_rich.cpp -g -Wall
// DONE

#include <bits/stdc++.h>
#include <set>
#include <algorithm>

std::string richieRich(std::string s, int n, int k)
{
    int i = n-1;
    int j = 0;
    int middle = n / 2;
    std::set<int> changed;
    int differences = 0;

    while (i >= middle)
    {
		if (s[i] != s[j])
		{
			differences++;
            if (k > 0)
			{
				int m = std::max(s[i], s[j]);
                s[i] = m;
				s[j] = m;
                k--;
                differences--;
                changed.insert(i);
                changed.insert(j);
			}                    
		}            
		j++;
        i--;
    }

	i = 0;
    j = n-1;
    while (k > 0 && j >= middle)
	{
		if (s[i] == s[j] && s[i] != '9')
		{
			if (changed.find(i) != changed.end() || changed.find(j) != changed.end())
			{
                s[i] = '9';
				s[j] = '9';
                k--;
			}
			else if(k > 1)
			{
                s[i] = '9';
				s[j] = '9';
                k-=2;	
			}
		}            
        i++;
        j--;
	}

	if (k == 1 && n % 2 != 0)
        s[middle] = '9';
    
    if (differences <= 0)
        return s;
    return "-1";   
}

int main() {
	int n;
	std::cin >> n;
	int k;
	std::cin >> k;
	std::string s;
	std::cin >> s;
	std::string result = richieRich(s, n, k);
	std::cout << result << std::endl;
	return 0;
}
