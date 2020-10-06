#include <iostream>
#include <string>
using namespace std;

class Character {
public:
	Character();
	~Character();

	int* CharacterAge;
	float* CharacterHealth;
};

int main() {

	Character* Char = new Character();
	delete Char;

	system("pause");
}

Character::Character() {
	cout << "A new character was created!\n";
	CharacterAge = new int(1);
	CharacterHealth = new float(100.f);
	cout << "Age is: " << *CharacterAge << endl;
	cout << "Health is: " << *CharacterHealth << endl;
}

Character::~Character() {
	cout << "Character destroyed!\n";
	delete CharacterAge;
	delete CharacterHealth;
}