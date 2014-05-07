#include <bits/stdc++.h>
#define mmm 2000000
using namespace std;

long long int A[2001][2001];
int main()
{
	A[0][0] = 1;
	for (int i =1;i < 2001; i++)
	{
		A[i][0] = 1;
		for(int j=1; j<=i;j++)
		{
			//ncr = n-1cr+n-1cr-1
			A[i][j] = A[i-1][j]+A[i-1][j-1];
		}
	}
	long long int ans = 2147483647;
	int mi;
	int mj;
	for(int i=0;i < 2001;i++)
	{
		for(int j = 0; j<2001;j++)
		{
			if(abs(A[i][2]*A[j][2]-mmm) < ans)
			{
				ans = abs(A[i][2]*A[j][2]-mmm);
				mi=i;
				mj=j;
			}
		}
	}
	cout<<mi<<" "<<mj<<endl;
}