#include <iostream>
using namespace std;
#define join(a,b) a*10+b
int main()
{
	for(int i= 1; i <= 9; i++)
	{
		for(int j =1; j <= 9; j++)
		{
			int k1 = join(i,j);
			for (int k = 1; k <=9; k++)
			{
				for (int l = 1; l <= 9; ++l)
				{
					int k2 = join(k,l);
					if(k1 < k2)
					{
						if( i==k || j==k || i == l || j == l)
						{
							int a = (i == k)? j : i;
							int b = (i == k)? k : l;
							int status = 1;
							for(int ad = 2; ad <= 100; ad++)
							{
								if(a*ad == k1 && b*ad == k2)
								{
									status = 0;
									break;
								}
							}
							if(status == 0)
							{
								cout<<k1<<"/"<<k2<<endl;
								cout<<a<<" "<<b<<endl;
							}
						}
					}
				}		
			}
		}
	}

	return 0;
}