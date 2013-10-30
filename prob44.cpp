#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;
int perfectSquare(long long n)
{
	int k = (int)(sqrt(n));
	if(k*k == n)
		return k;
	else
		return -1;
}
bool ispentagonal(int n)
{
	if(perfectSquare(1+(24*n)) != -1)
	{
		if(perfectSquare(1+24*n)%6 == 5)
			return true;
	}
	return false;
}
int main()
{
	int result = 0;
	bool notFound = true;
	int i = 1;
	 
	while (notFound) 
	{
	    i++;
	    int n = i * (3 * i - 1) / 2;
	    for (int j = i-1; j > 0; j--) 
	    {
	        int m = j * (3 * j - 1) / 2;
	        if (ispentagonal(n - m) && ispentagonal(n + m)) 
	        {
	            result = n-m;
	            notFound = false;
	            break;
	        }
	    }
	}
	cout<<result<<endl;
	return 0;
}