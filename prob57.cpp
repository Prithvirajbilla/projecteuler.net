#include <iostream>
#include <math.h>
using namespace std;

unsigned int nod(unsigned int n)
{
	return (int)log10((double) n) +1;
}
int main()
{
	long long num = 3;
	long long dec = 2;
	int ans = 0;
	for(int i= 0; i< 999; i++)
	{
		long long tem = num;
		num += (2* dec);
		dec +=tem;
		cout<<num<<"/"<<dec<<endl;
		if(nod(num) > nod(dec))
		{
			ans++;
		}
	}
	cout<<ans<<endl;
	return 0;
}