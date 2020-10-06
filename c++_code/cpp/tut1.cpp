#include <iostream>
using namespace std;//allows not having to always precede function calls with std

int main() {
	//std::cout << "You died!\n";
	char myCharacter;
	myCharacter = 'y';

	int myInt;
	myInt = 13;

	cout << myCharacter << "\n";
	cout << myInt << endl;

	myCharacter = 'n';
	myInt = 17;

	cout << myCharacter << "\n";
	cout << myInt << endl;

	system("pause");
}