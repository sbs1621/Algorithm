#include <iostream>
using namespace std;

int gcd(int a, int b)//최대공약수
{
	int c;
	while (b != 0)
	{
		c = a % b;
		a = b;
		b = c;
	}
	return a;
}

int main()
{
	int a, b;
	cin >> a >> b;
	
	cout << gcd(a, b) << endl << (a * b) / gcd(a, b);
		
}
