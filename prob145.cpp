#include <iostream>
#include <math.h>
using namespace std;

long long reverse(long long num)
{
	long long rev = 0;
	while(num > 0)
	{
		rev = rev*10 + num%10;
		num/=10;
	}
	return rev;
}
bool odd(long long num)
{
	while(num > 0)
	{
		if((num%10)%2 == 0)
			return false;
		num/=10;
	}
	return true;
}
int main()
{
	int sum = 0;
	for(long long i = 1001; i< 1000000000 ; i++)
	{
		if(i%10 != 0)
		{
			if(odd(i+reverse(i)))
			{
				sum++;
			}
		}
	}
	cout<<sum+120<<endl;
	return 0;
}