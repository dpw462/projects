#include <iostream>
#include <string>
using namespace std;

int main() {

	char myCString1[5] = { 'D','o','g','s','\0' };
	char myCString2[5] = "Dogs";
	cout << myCString1 << endl;
	cout << myCString2 << endl;

	string myString, first, last;
	myString = "My dog's name is ";
	first = "Spot ";
	last = "Jones";
	//myString += first;
	//myString += last;
	myString += (first + last);

	cout << myString << endl;



	system("pause");
}