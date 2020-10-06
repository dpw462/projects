#include <iostream>
#include <string>
using namespace std;

void Print(string str);
void Print(int i);
void Print(string str1, string str2);
void Print(int i, string str);

int main() {

	//Print(3);
	//Print("My string 1!", "My string 2!");
	//Print(5, "My string!");
	
	int myInt = 1;
	string myStr = "Alan";
	string mySecondStr = "Jones";
	
	Print(myStr);
	Print(mySecondStr);
	Print(myInt);
	Print(myInt, mySecondStr);
	Print(myStr, mySecondStr);

	system("pause");
}

void Print(string str) {
	
	cout << str << endl;
}

void Print(int i) {
	cout << i << endl;
}

void Print(string str1, string str2) {
	cout << "String 1: " << str1 << endl;
	cout << "String 2: " << str2 << endl;
}

void Print(int i, string str) {
	cout << "Integer: " << i << endl;
	cout << "String: " << str << endl;

}