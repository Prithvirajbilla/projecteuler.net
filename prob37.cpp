#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;
bool isprime(long long n)
{
	if(n <= 1)
		return false;
	if(n == 2)
		return true;
	for(int i = 2; i<= ceil(sqrt(n)) + 1; i++)
	{
		if(n%i == 0)
			return false;
	}
	return true;
}

int main(int argc, char const *argv[])
{
	vector<long long> prime;
	long long i = 2;
	long long sum = 0;
	int kl = 0;
	while(true)
	{
		if(isprime(i))
		{
			prime.push_back(i);
			long long num = i;
			num = num/10;
			int status = 0;
			while(num >0)
			{
				if(find(prime.begin(), prime.end(),num) != prime.end() || prime[prime.size()-1]==num)
				{
					status = 1;
					num= num/10;
				}
				else
				{
					status = 0;
					break;
				}
			}
			int status1 = 0;
			int no = 10;
			long long num1 = i%10;
			while(true)
			{
				if(find(prime.begin(), prime.end(),num1) != prime.end() || prime[prime.size()-1]==num1)
				{
					status1 = 1;
					no = no*10;
					num1 = i%no;
				}
				else
				{
					status1 = 0;
					break;
				}

				if(num1 == i)
					break;
			}
			if(status1 == 1 && status == 1)
			{
				cout<<i<<endl;
				kl++;
			}
			if(kl == 11)
				break;

		}
		i++;
	}
	return 0;
}