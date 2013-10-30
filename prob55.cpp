#include <iostream>
#include <math.h>
using namespace std;
bool ipal(long long n)
{
	long long rev  = 0;
	long long k = n;
	while( n > 0)
	{
		rev = rev*10 + n%10;
		n = n/10;
	}
	if(k == rev)
		return true;
	else
		return false;

}
long long reverse(long long n)
{
	long long rev  = 0;
	long long k = n;
	while( n > 0)
	{
		rev = rev*10 + n%10;
		n = n/10;
	}
	return rev;
}
int main()
{
	long long ans = 0;
	for(int i =1; i <= 10000;i++)
	{
		int loopcount = 0;
		long long start = i + reverse(i);
		while(loopcount < 50)
		{
			if(ipal(start))
			{
				ans++;
				break;
			}
			else
			{
				start = start+ reverse(start);
			}
			loopcount++;
		}	
	}

	cout<<ans<<endl;
	return 0;
}