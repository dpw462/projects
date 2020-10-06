#include <iostream>
using namespace std;

void Welcome() {
	cout << "Welcome!\n";
}

void printNumber(int numToPrint) {
	cout << "Your number is "<< numToPrint << endl;
}

int add(int a, int b) {
	int result;
	result = a + b;
	
	return result;
}

int main() {

	Welcome();
	printNumber(4);
	int c;
	c = add(1, 4);
	printNumber(c);
	
	system("pause");
}