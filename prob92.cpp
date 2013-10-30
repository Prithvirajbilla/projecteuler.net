#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long digitSquare(long long num)
{
	long long ans = 0;
	while(num > 0)
	{
		ans = ans  + (num%10)*(num%10);
		num = num/10;
	}
	return ans;
}

int main()
{
	int* array = new int[10000000];
	//0 for one
	//1 for 89
	//2 intially
	fill(array,array+10000000,2);
	array[0] = 0;
	array[88] = 1;
	for(int i=0;i < 10000000; i++)
	{
		if(array[i] == 2)
		{
			vector<int> v;
			int k = i+1;
			while(k != 1 && k != 89)
			{
				v.push_back(k);
				k = digitSquare(k);
				if(array[k-1] != 2)
				{
					break;
				}
			}
			int awe = array[k-1];
			if (k == 1 )
				awe = 0;
			else if(k == 89)
				awe = 1;
			for(int kl = 0; kl < v.size() ; kl++)
			{
				array[v[kl]-1] = awe;
			}
		}
	}
	int count = 0;
	for (int i = 0; i < 10000000; ++i)
	{
		if(array[i] == 1)
			count++;
	}
	cout<<count<<endl;
	return 0;
}