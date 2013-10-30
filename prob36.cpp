#include <iostream>
#include <bitset>
using namespace std;
bool palindrome(int a)
{
	int rev = 0;
	int k = a;
	while(a > 0)
	{
		rev = rev*10+a%10;
		a= a/10;
	}
	if(rev == k)
		return true;
	else
		return false;
}
bool palb(unsigned int n)
{
    unsigned m = 0;

    for(unsigned tmp = n; tmp; tmp >>= 1)
    	m = (m << 1) | (tmp & 1);

    return m == n;
}
int main(int argc, char const *argv[])
{
	long long sum = 0;
	cout<<palb(525)<<endl;
	for(int i=0; i< 1000000; i++)
	{
		if(palindrome(i) == true)
		{
			if(palb(i) == true)
			{
				sum+=i;
			}
		}
	}
	cout<<sum<<endl;
	return 0;
}