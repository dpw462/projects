#include <iostream>
#include <string>
using namespace std;

enum PlayerStatus {
	PS_Crouched,
	PS_Standing,
	PS_Walking,
	PS_Running
};//useful for describing STATES, not necessarily the int value of the enum constants

enum MovementStatus {
	MS_Crouched,
	MS_Running
};

int main() {

	PlayerStatus status;
	status = PlayerStatus::PS_Running;
	
	if (status == PS_Crouched) {
		cout << "The player is crouching!\n";
	}
	status = PS_Running;
	if (status == PS_Crouched) {
		cout << "The player is crouching!\n";
	}


	system("pause");
}