#include <iostream>
#include <string>
using namespace std;

struct Container {
	int x, y, z;
	string Name;
};

int main() {
	/*
	int* aptr; 
	int a = 100;
	aptr = &a;
	cout << aptr << endl;
	cout << *aptr << endl;
	int b = 50;
	aptr = &b;
	cout << aptr << endl;
	cout << *aptr << endl;
	*/
	/*
	int numbers[] = { 0,1,2,3,4,5,6,7,8,9,10 };
	int* NumPtr;
	NumPtr = numbers;

	cout << NumPtr << endl;
	cout << *NumPtr << endl;
	NumPtr++;
	cout << *NumPtr << endl;
	NumPtr += 3;
	cout << *NumPtr << endl;
	*/

	Container container = { 5, 6, 7, "Sam" };
	Container* ptrToCont = &container;
	cout << (*ptrToCont).Name << endl;
	cout << (*ptrToCont).x << endl;
	cout << (*ptrToCont).y << endl;
	cout << (*ptrToCont).z << endl;
	cout << ptrToCont->Name << endl;//arrow notation; "syntactical sugar"; most commonly used!
	cout << ptrToCont->x << endl;
	cout << ptrToCont->y << endl;
	cout << ptrToCont->z << endl;


	system("pause");
}