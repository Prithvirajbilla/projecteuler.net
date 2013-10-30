#include <iostream>
#include <algorithm>
using namespace std;
#define m(a,b,c) a*100+b*10+c
int main()
{
	long long sum = 0;
	int* array = new int[10];
	for(int i=0; i < 10; i++)
	{
		array[i] = i;
	}
	do
	{
		int a = m(array[1],array[2],array[3]);
		int b = m(array[2],array[3],array[4]);
		int c = m(array[3],array[4],array[5]);
		int d = m(array[4],array[5],array[6]);
		int e = m(array[5],array[6],array[7]);
		int f = m(array[6],array[7],array[8]);
		int g = m(array[7],array[8],array[9]);
		if(a%2 ==0  && b%3 ==0 && c%5 == 0 && d%7 == 0 && e%11 == 0 && f%13 == 0 && g%17 == 0)
		{
			long long k = 0;
			for(int i=0; i< 10; i++)
			{
				k = k*10+ array[i];
			}
			sum+=k;
		}

	}
	while(next_permutation(array,array+10));
	cout<<sum<<endl;
	return 0;
}