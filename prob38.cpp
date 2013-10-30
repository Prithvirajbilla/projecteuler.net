#include <iostream>
using namespace std;
bool isPandigital(int n)
{
    int digits = 0; int count = 0; int tmp;

    for (; n > 0; n /= 10, ++count)
    {
        if ((tmp = digits) == (digits |= 1 << (n - ((n / 10) * 10) - 1)))
            return false;
    }

    return digits == (1 << count) - 1;
}
int concat(int x,int y)
{
    unsigned po = 10;
    while(y >= po)
        po *= 10;
    return x * po + y;        }
int main()
{
	int i = 1;
	long result = 0;
	for (long i = 9387; i >= 9234; i--) 
	{
	    result = concat(i, 2*i);
	    if(isPandigital(result)){
	        break;
    }
	}
	cout<<result<<endl;

}