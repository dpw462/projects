#include <iostream>
#include <string>
using namespace std;

int main() {

	//int myIntArray[10];
	//int index_array;
	int myArray[5] = { 1, 23, 5, 4, 9 };

	for (int i = 0; i < 5; i++) {
		//myIntArray[i] = i;
		//cout << myIntArray[i] << endl;
		cout << "myArray[" << i << "] = " << myArray[i] << endl;
	}



	/*
	cout << "Which element in the 10-d array do you want? ";
	cin >> index_array;
	cout << "Element " << index_array <<" is: " << myIntArray[(index_array-1)] << endl;
	cout << "My array element 1: " << myArray[0] << endl;
	cout << "My array element 2: " << myArray[1] << endl;
	cout << "My array element 3: " << myArray[2] << endl;
	cout << "My array element 4: " << myArray[3] << endl;
	cout << "My array element 5: " << myArray[4] << endl;
	//expect nonsense/out of bounds data
	//cout << "My array element 6: " << myArray[5] << endl;
	*/

	system("pause");
}