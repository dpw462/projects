#include <iostream>
using namespace std;

int main() {

	int i = 3;
	//--i;
	//i--;
	//float j = 2.0;

	//float k = j / i;
	cout << "Using pre-decrement: " << --i << endl;
	cout << i << endl;
	cout << "Using post-increment: " << i++ << endl;
	cout << i << endl;

	system("pause");
}