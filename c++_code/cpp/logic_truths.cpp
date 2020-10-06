#include <iostream>
#include <string>
using namespace std;

int main() {

	int i = 1;
	int j = 2;
	int k = 3;

	if (i == k || i == j) {
		cout << "this will never be printed" << endl;
	}

	if (i <= k && i < j) {
		cout << "this will be printed" << endl;
	}


	system("pause");
}