#include <iostream>
using namespace std;

int main() {

	int a(13);//parentheses notation
	int b = 13;//assignment operator

	if (b < a) {
		cout << "a is less than b." << endl;

	}
	else if ( a < b) {
		cout << "a is less than b." << endl;
	}
	else {
		cout << "a is equal to b." << endl;
	}

	system("pause");
}