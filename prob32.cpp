#include <iostream>
using namespace std;
int sum = 0;
#define mke2(a,b) a*10+b
#define mke3(a,b,c) a*100+b*10+c
#define mke4(a,b,c,d) a*1000+mke3(b,c,d)
void swap(int* a,int* b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}
void permutate(int* array,int i, int j)
{
	if(i == j)
	{
		int a = mke2(array[7],array[8]);
		int b = mke3(array[4],array[5],array[6]);
		int c = mke4(array[0],array[1],array[2],array[3]);
		if(a*b == c)
		{
			sum+=c;
			cout<<a<<" "<<b<<" "<<c<<endl;
		}

		a = array[8];
		b =  mke4(array[0],array[1],array[2],array[3]);
		c =  mke4(array[4],array[5],array[6],array[7]);
		if(a*b == c)
		{
			sum+=c;
			cout<<a<<" "<<b<<" "<<c<<endl;
		}
		

	}
	else
	{
		for(int k = i; k <=j ;k++)
		{
			swap(&array[i],&array[k]);
			permutate(array,i+1,j);
			swap(&array[i],&array[k]);
		}
	}
}
int main()
{
	int* array = new int[9];
	for(int i =0;i < 9; i++)
		array[i] = i+1;

	permutate(array,0,8);
	cout<<sum<<endl;


}