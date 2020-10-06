#include <iostream>
#include <string>
using namespace std;

struct LocationVector {
	float X, Y, Z;
};

struct Player {
	int Level;
	float Health, Damage, Stamina;
	
	LocationVector Location = { 0.f,0.f,0.f };//default locaton at origin

	void TakeDamage(float dmg) {
		Health -= dmg;
	}

	int GetLevel() {
		if (Level > 10) {
			cout << "Level is greater than 10! \n";
		}
		return Level;
	}

	void DisplayLocation() {
		cout << "Location X = "<< Location.X << endl;
		cout << "Location Y = "<< Location.Y << endl;
		cout << "Location Z = "<< Location.Z << endl;
	}

};

int main() {

	Player p1;
	p1.Level = 11;
	p1.Health = 100.f;
	p1.Damage = 10.f;
	p1.Stamina = 20.f;

	//cout << "Player 1 Level = " << p1.Level << endl;//bad practice to call variables directly
	cout << "Player 1 Level = " << p1.GetLevel() << endl;//good practice; use function to call from struct so that updates are seamless, more below
	p1.TakeDamage(40.f);
	cout << "Player 1 takes " << 40.f << " damage!" << endl;
	cout << "Player 1 Health = " << p1.Health << endl;
	p1.DisplayLocation();

	Player p2 = { 1,50.f,40.f,35.54f,{35.5f, 67.45f, 100.003f} };
	p2.DisplayLocation();

	system("pause");
}