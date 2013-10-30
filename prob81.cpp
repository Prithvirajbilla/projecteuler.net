#include <iostream>
using namespace std;
int getmin(int array[][80],int i ,int j )
{
	if(i == 79 && j == 79)
	{
		return array[i][j];
	}
	else if(i >79)
	{
		return 2147483647;
	}
	else if( j > 79)
	{
		return 2147483647;
	}
	else
	{
		int k = getmin(array,i+1,j);
		int f = getmin(array,i,j+1);
		k	= (k < f)?k:f;
		int min= k+array[i][j];
		cout<<min<<":"<<i<<":"<<j<<endl;
		return min;
	}
}
int main(int argc,char const *argv[])
{
	int array[80][80];
	for(int i = 0; i < 80;i++)
	{
		for (int j = 0; j < 80; ++j)
		{
			cin>>array[i][j];
		}
	}
	int min = 0;
	cout<<getmin(array,0,0)<<endl;;
	return 0;
}
