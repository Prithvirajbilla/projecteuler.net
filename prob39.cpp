#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int p = 12;
	long long* array = new long long[1001];
	for(int i =0; i< 1001; i++)
	{
		array[i] = i*i;
	}
	int* arr = new int[3000];
	fill(arr,arr+3000,0);
	for(int i=0;i < 1000;i++)
	{
		for(int j = i+1; j < 1000; j++)
		{
			long long sqc = array[j]+array[i];
			long long* f = find(array,array+1001,sqc);
			if( f != array+1001 || array[1000] == sqc)
			{
				arr[f-array+i+j]++;
			}
		}
	}
	cout<<max_element(arr,arr+1000)-arr<<endl;
	return 0;
}