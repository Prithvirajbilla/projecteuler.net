#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	long long i = 99;
	while(true)
	{
		i++;
		pair<int,int> array[10];
		fill(array,array+14,pair<int,int>(0,0));
		long long k = i;
		int s = 1;
		while(k > 0)
		{

			array[k%10]= pair<int,int>(1,array[k%10].second+1);
			k = k/10;
		}
		long long i2 = 2*i;
		k = i2;
		while(k > 0)
		{
			if(array[k%10].first != 1)
			{
				s = 0;
				break;
			}
			k=k/10;
		}
		long long i3 = 3*i;
		k = i3;
		while(k > 0)
		{
			if(array[k%10].first != 1)
			{
				s = 0;
				break;
			}
			k=k/10;
		}
		long long i4 = 4*i;
		k = i4;
		while(k > 0)
		{
			if(array[k%10].first != 1)
			{
				s = 0;
				break;
			}
			k=k/10;
		}
		long long i5 = 5*i;
		k = i5;
		while(k > 0)
		{
			if(array[k%10].first != 1)
			{
				s = 0;
				break;
			}
			k=k/10;
		}
		long long i6 = 6*i;
		k = i6;
		while(k > 0)
		{
			if(array[k%10].first != 1)
			{
				s = 0;
				break;
			}
			k=k/10;
		}
		if(s == 1)
		{
			cout<<i<<endl;
			break;
		}
	}
	return 0;
}