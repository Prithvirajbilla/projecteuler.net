#include <iostream>
#include <math.h>
using namespace std;
bool isprime(long long n)
{
	if(n <= 1)
		return false;
	if(n <= 3)
		return true;
	for(int i=2; i<= ceil(sqrt(n))+1; i++)
	{
		if(n%i == 0)
			return false;
	}
	return true;
}

int distinct(long long n)
{
	int d = 0;
	int i = 2;
	while( n > 0 && n >= i)
	{
		if(isprime(i) == true)
		{
			if(n%i == 0)
				d++;
			while(n%i == 0)
			{
				n = n/i;
			}
		}
		i++;
	}
	return d;
}
int main()
{
	long long i =210;
	while(true)
	{
		if(distinct(i) == 4 && distinct(i+1) == 4 && distinct(i+2) == 4 && distinct(i+3) == 4)
			break;
		cout<<i<<endl;
		i++;
	}
	cout<<i<<endl;
	return 0;
}