# /*#include <bits/stdc++.h>

# using namespace std;

# int num(long long int a)
# {
# 	int i = 0;
# 	while( a> 0)
# 	{
# 		i++;
# 		a=a/10;
# 	}
# 	return i;
# }

# int main(int argc, char const *argv[])
# {
# 	int a = 1;
# 	int b = 2;
# 	int answer = 0;
# 	for (int i = 0; i < 1000; ++i)
# 	{
# 		long long int a1 = (2*b) + a;
# 		long long int b1 = b+a;
# 		if(num(a1)>num(b1))
# 			answer++;
# 		a = a1;
# 		b = b1;
# 		cout<<a<<"/"<<b<<endl;
# 	}
# 	cout<<answer<<endl;
# 	return 0;
# }*/

a = 3;
b = 2;
answer = 0;
for i in range(999):
	a,b=(2*b)+a,b+a;
	if len(str(a)) > len(str(b)):
		print a,"/",b
		answer=answer+1
print answer