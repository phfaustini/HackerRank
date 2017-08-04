//https://www.hackerrank.com/challenges/is-fibo
// g++ -std=c++11 -g isFibo.cpp
// DONE
#include<iostream>
#include<vector>

int main()
{
	long numbers;
	std::cin >> numbers;
	std::vector<long> fib;
	fib.push_back(0); fib.push_back(1); fib.push_back(1);
	while (numbers--)
	{
		long candidate;
		std::cin >> candidate;
		bool is = false;
		if (candidate > fib[fib.size() - 1])
		{
			long max_fib = fib[fib.size() - 1];
			while (candidate > max_fib)
			{
				max_fib = fib[fib.size() - 1] + fib[fib.size() - 2];
				fib.push_back(max_fib);
				if (max_fib == candidate)
				{
					is = true;
					break;
				}
			}
		}
		else
		{
			for (unsigned i(0); i < fib.size(); i++)
				if (fib[i] == candidate)
				{
					is = true;
					break;
				}
		}
		if (is) std::cout << "IsFibo" << std::endl;
		else std::cout << "IsNotFibo" << std::endl;
	}
    return 0;
}
