#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;
bool isprime(int n)
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

int main()
{
	vector<int> prime ;
	for(int i =1000 ; i< 9999; i++ )
	{
		if(isprime(i))
		{
			prime.push_back(i);
		}
	}
	for(int i =0; i< prime.size(); i++)
	{
		int number = prime[i];
		int array[4];
		for(int j =3 ; j >= 0; j--)
		{
			array[j] = number%10;
			number = number/10;
		}
		number = prime[i];
		int p[24];
		int km = 0;
		do
		{	
			p[km] = array[0]*1000+array[1]*100+array[2]*10+array[3];
			km++;
		}while(next_permutation(array,array+4));

		for(int nk = 1; nk < 24; nk++)
		{
			int num = p[nk];
			if(find(prime.begin(), prime.end(),num) != prime.end() || prime[prime.size()-1]==num)
			{
				int dif = num - number;
				for(int nkk=nk+1; nkk < 24; nkk++)
				{
					int num1= p[nkk];
					if(find(prime.begin(), prime.end(),num1) != prime.end() || prime[prime.size()-1] == num1)
					{
						if(num1-num == dif)
						{
							cout<<number<<":"<<num<<":"<<num1<<endl;
						}
					}
				}

			}
		}
	}
	return 0;
}