#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;

long long sumDiv(int n)
{
	long long sum = 1;
	for (int i = 2; i < n; ++i)
	{
		if(n%i == 0)
		{
				sum= sum+ i;
		}
	}
	return sum;
}

int main(int argc, char const* argv[])
{
	bool* array = new bool[28124];   //one byte 
	bool* abundant = new bool[28124]; //one byte !!!

	fill(abundant,abundant+28124,0);
	fill(array,array+28124,0);
	for(int i = 0; i < 28124; i++)
	{
		if(sumDiv(i+1) > i+1)
		{
			abundant[i] = 1;
		}

	}
	for(int i = 0; i < 28124; i++)
	{
		for(int j =i ; j < 28124; j++)
		{
			if(abundant[i] == 1 && abundant[j] == 1)
			{
				int k = i+j+2;
				if(k-1 < 28124)
				{
					array[k-1] = 1;
				}
			}
		}
	}
	long long sum = 0;
	for (int i = 0; i < 28124; ++i)
	{
		if(array[i] == 0)
		{
			sum = sum+i+1;
		}
	}
	cout<<sum<<endl;

	return 0;
}