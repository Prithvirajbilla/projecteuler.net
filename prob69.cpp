#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	double max = 0;
	int max_num = 0;
	for (int i = 2; i < 1000000; ++i)
	{
		int n= i;  //this is the number you want to find the totient of
		int tot = n; //this will be the totient at the end of the sample
		for (int p = 2; p*p <= n; p++)
		{
		    if (n%p==0)
		    {
		        tot /= p;
		        tot *= (p-1);
		        while ( n % p == 0 ) 
		            n /= p;
		    }
		}
		if ( n > 1 ) { // now n is the largest prime divisor
		    tot /= n;
		    tot *= (n-1);
		}
		double ans = i;
		ans = ans/tot;
		if(ans>max)
		{
			max = ans;max_num=i;
		}
/*		cout<<i<<" "<<ans<<" "<<tot<<endl;
*/	}
	cout<<max_num<<endl;
	return 0;
}