#include <iostream>
#include <string>
using namespace std;

/* USING STATIC CAN ALLOW FOR FUNCTIONS TO BE CALLED WITHOUT INSTANTIATING OBJECT OF CLASSES */

//1. using static with function
void AddToCount() {
	static int count = 0;//memory will not be cleared until entire program is done
	count++;
	cout << count << endl;
}
//2. using static with class
class Item {
public:
	Item() {
		cout << "An item has been created!\n";
	}
	~Item() {
		cout << "An item has been destroyed!\n";
	}
};
//3. using static with var's inside class
class Critter {
public:
	Critter() {
		cout << "A critter is born!\n";
		++CritterCount;
	}

	//4.
	static void AnnounceCount() {
		cout << CritterCount << endl;
	}

	static int CritterCount;//cannot initialize static inside class unless const
};
int Critter::CritterCount = 0;//initialized here
//4. using static with functions in class (see above class)

int main() {
	//1.
	AddToCount();
	AddToCount();//notice how you cannot re-initialize variables because static, therefore 1 became 2, became 3, etc...
	//
	//2.
	static Item item;
	//

	//3.
	Critter crit;
	Critter::AnnounceCount();
	//Critter::CritterCount = 13;
	//cout << Critter::CritterCount << endl;
	Critter crit2;
	Critter::AnnounceCount();
	//cout << Critter::CritterCount << endl;
	Critter* crit3 = new Critter;
	Critter::AnnounceCount();
	delete crit3;


	system("pause");
}