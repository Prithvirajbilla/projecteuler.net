#include <iostream>
#include <math.h>
using namespace std;
unsigned no (unsigned i)
{
    return i > 0 ? (int) log10 ((double) i) + 1 : 1;
}

int main()
{
	int i = 1;
	long long sum = 1;
	int k  = 1;
	int prod=1;
	while(true)
	{
		if(i == 1000000)
			break;
		if(sum >= i)
		{
			cout<<sum<<":"<<k<<endl;
			int s = sum-i-1;
			int ans = k%10;
			int rec = k/10;
			while(s>0)
			{
				
				ans = k%10;
				s--;
				rec=rec/10;
			}
			rec=rec%10;
			cout<<rec<<" "<<endl;
			i = i*10;
		}

		k++;
		sum+=no(k);
	}
}