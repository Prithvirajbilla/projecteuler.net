#include <iostream>
#include <math.h>
using namespace std;
#define MAX 100
long long triangle[MAX + 1][MAX + 1];
int ans;
void makeTriangle() {
    int i, j;

    ans = 0;
    triangle[0][0] = 1; 
    for(i = 1; i < MAX+1; i++) {
        triangle[i][0] = 1; 
        for(j = 1; j <= i; j++) {
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            if(triangle[i][j] > 1000000)
            {
            	triangle[i][j] = 1000001;
            	ans++;
            }
        }
    }
}
int main()
{
	makeTriangle();
	cout<<ans<<endl;
}