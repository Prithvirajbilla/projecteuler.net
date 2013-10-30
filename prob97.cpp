#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	long long k  = 10000000000;
	long long sum = 1;
	for(int i = 0 ; i < 7830457; i++)
	{
		sum = sum*2;
		sum= sum%k;
	}
	sum = (sum*28433)%k;
	sum = (sum+1)%k;
	cout<<sum<<endl;

	return 0;
}