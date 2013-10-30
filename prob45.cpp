#include <iostream>
using namespace std;

int main()
{
	long long n1 = 1;
	long long n2 = 1;
	long long n3 = 1;
	int s = 0;
	while(true)
	{
		long long h = n3*((2*n3)-1);
		long long p = n2*((3*n2)-1)/2;
		long long t = n1*(n1+1)/2;
		while(t < h)
		{
			n1++;
			t = n1*(n1+1)/2;
		}
		while(p < h)
		{
			n2++;
			p = n2*((3*n2)-1)/2;
		}
		if(p == h && h==t)
		{
			if(s==3)
			{
				break;
			}
			cout<<p<<" "<<h<<" "<<t<<endl;
			s++;

		}
		n3++;

	}
}