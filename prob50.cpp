#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
using namespace std;

bool isprime(int n)
{
	if(n <= 1)
		return false;
	if(n <= 3)
		return true;
	for(int i= 2; i<= ceil(sqrt(n)) +1; i++)
	{
		if(n%i == 0)
			return false;
	}
	return true;
}
int main()
{

	vector<int> v;
	for(int i =1; i<= 1000000; i++)
	{
		if(isprime(i))
			v.push_back(i);
	}
	int max = 0;
	int kl;
	for(int i =0; i< v.size(); i++)
	{
		long long sum = v[i];
		 kl = 1;
		for(int j= i+1 ; j < v.size(); j++)
		{
			sum+=v[j];
			if(sum%2 == 0)
			{
				kl++;
				continue;
			}
			if(find(v.begin(),v.end(),sum) != v.end() && v[v.size()-1] == sum)
			{
				if(kl > max)
				{
					max = kl;
				}
			}
			kl++;

		}
		cout<<max<<":"<<i<<":"<<sum<<endl;
	}
	cout<<kl<<endl;
	return 0;
}