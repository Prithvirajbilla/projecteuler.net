#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	long long* array = new long long [10];
	for(int i = 0; i < 10; i++)
	{
		array[i] = i*i*i*i*i;
	}
	// for(int i =0 ; i< 10; i++)
	// {
	// 	cout<<array[i]<<" ";
	// }
	long long sum = 0;
	for(int i =0 ; i < 99999999; i++)
	{
		int k = i;
		int s = 0;
		while(k != 0)
		{
			s+=array[k%10];
			k = k/10;
		}
		if(s == i)
		{
			sum+=i;
			cout<<i<<endl;
		}
	}
	cout<<sum<<endl;
	return 0;
}