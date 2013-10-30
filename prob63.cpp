#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	int sum = 0;
	long long s = 0;
	int n = 1;
	while( s <= 10)
	{
		s = (int)(ceil(pow(10,(float)(n-1.0)/(float) n)));
		sum+= 10 - s;
		n++;
	}
	cout<<sum<<endl;
}