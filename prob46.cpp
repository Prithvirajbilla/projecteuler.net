#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
using namespace std;
typedef vector<long long> vi;
bool isprime(long long n)
{
	if(n <= 1)
		return false;
	if(n <= 3)
		return true;
	for(int i = 2; i<= ceil(sqrt(n))+ 1; i++)
	{
		if(n%i == 0)
			return false;
	}
	return true;
}

int main()
{
	vector<long long> prime;
	vector<long long> square;
	square.push_back(1);
	long long i = 2;
	while(true)
	{
		square.push_back(i*i);
		if(i%2 == 1)
		{
			if(isprime(i))
			{
				prime.push_back(i);
			}
			else
			{
				int sta= 0;
				for(int k = 0; k < prime.size() ; k++)
				{
					long long diff = (i - prime[k])/2;
					if(find(square.begin(),square.end(),diff) != square.end())
					{
						sta = 1;
						break;
					}
				}
				if(sta == 0)
				{
					cout<<i<<endl;
					break;
				}
				cout<<i<<endl;

			}	
		}
		i++;
	}
}