#include <iostream>
#include "Object.h"
#include "Actor.h"
#include "Pawn.h"
using namespace std;

void InheritanceFunction();

int main() {

	InheritanceFunction();
	system("pause");
}

void InheritanceFunction() {

	Object* ptr_to_obj = new Object;
	Actor* ptr_to_act = new Actor;
	Pawn* ptr_to_pwn = new Pawn;

	Object* ObjectArray[] = { ptr_to_obj,ptr_to_act,ptr_to_pwn };
	for (int i = 0; i < 3; i++) {
		Object* obj = ObjectArray[i];
		Actor* act = dynamic_cast<Actor*>(obj);//casting the object; if cast failed, will return null
		if (act) {
			act->ActorFunction();
		}
		Pawn* pwn = dynamic_cast<Pawn*>(obj);
		if (pwn) {
			pwn->PawnFunction();
		}
	}

	delete ptr_to_obj;
	delete ptr_to_act;
	delete ptr_to_pwn;
}
