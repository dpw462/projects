#include <iostream>
#include <string>
using namespace std;

struct Character {

	Character();//calling constructor
	void PrintHealth();

	string Name;
	float Health;

};

//runtime created objects/vars are stored on the heap
int main() {

	for (int i = 0; i < 10; i++) {
		Character* PtrToChar = new Character();//stored on the heap; dynamic mem and will need to use DELETE to free mem after
		PtrToChar->Name = "Neo";
		cout << PtrToChar->Name << endl;
		PtrToChar->PrintHealth();
		delete PtrToChar;//this will free mem on the heap
	}
	
	system("pause");
}

//defined constructor
Character::Character(){
	Name = "Default Name";
	Health = 100.f;
}

void Character::PrintHealth() {
	cout << "Health = " << Health << endl;
}