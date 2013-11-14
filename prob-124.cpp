#include <iostream>
#include <algorithm>
#include <utility>
using namespace std;
struct myobj
{
	bool operator() (const pair<int,int> &v1,const pair<int,int> &v2)
	{
		return v1.second < v2.second;
	}
};
int main()
{
	bool* s = new bool[100001];
	fill(s,s+100001,true);
	s[0]= false;
	s[1] = false;
	for(int i=2; i < 100001;i++)
	{
		if(s[i])
		{
			int k;
			for(k = 2*i; k < 100001;)
			{
				s[k] = false;
				k+=i;
			}
		}
	}
	pair<int,int>* array = new pair<int,int>[100001];
	array[0] = pair<int,int>(0,0);
	for(int i=1; i<100001;i++)
	{
		int prod=1;
		int N = i;
		for(int k=1;k<100001 && N >0;k++)
		{
			if(s[k])
			{
				if(N%k ==0)
					prod = prod*k;
				while(N%k == 0)
				{
					N=N/k;
				}
			}
		}
		array[i] = pair<int,int>(i,prod);
	}

	stable_sort(array,array+100001,myobj());
	for(int i=0; i<100001; i++)
	{
		cout<<array[i].first<<" "<<array[i].second<<endl;
	}
	cout<<array[10000].first<<endl;
	return 0;
}