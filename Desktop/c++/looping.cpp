#include <iostream>
using namespace std;



int main() {

	for (int i = 0; i <= 10; i++) {
		for (int j = 0; j <= 10; j++) {
			for (int k = 0; k < 10; k++) {
				cout << "i = " << i << ", j = " << j << ", k = " << k << endl;
			}			
		}
	}

	cout << endl;
	
	/*
	//int myInt(0);
	//int count = 0;
	double num_pi = 3.1459265358;
	double num_e = 2.7182818284;
	bool Condition = true;

	do {
		cout << endl;
		cout << "The number PI is: " << num_pi << endl;
		cout << "The number E is: " << num_e << endl;
		cout << "Count is: " << count << endl;
		cout << "Pi + E * count is: " << (num_pi + num_e * count) << endl;

		count++;
		if (count <= 100) {
			Condition = true;
		}
		else {
			Condition = false;
		}
			
	} while (Condition);
	*/
	/*
	while (count <= 10) {
		cout << myInt << endl;
		myInt++;
		count++;
	}
	*/
	system("pause");
}