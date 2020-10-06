#include <iostream>
#include <string>
using namespace std;

class Object {
public:
	virtual void BeginPlay();

	void ObjectFuncion() {
		cout << "ObjectFunction() called! \n\n";
	}
};

class Actor : public Object {
public:
	virtual void BeginPlay() override;

	void ActorFunction() {
		cout << "ActorFunction called! \n\n";
	}
};

class Pawn : public Actor {
public:
	virtual void BeginPlay() override;

	void PawnFunction() {
		cout << "PawnFunction called! \n\n";
	}
};

int main() {

	Object* ptr_to_obj = new Object;
	Actor* ptr_to_act = new Actor;
	Pawn* ptr_to_pwn = new Pawn;

	Object* ObjectArray[] = { ptr_to_obj,ptr_to_act,ptr_to_pwn };
	for (int i = 0; i < 3; i++) {
		//ObjectArray[i]->BeginPlay();
		//ObjectArray[i]->ObjectFuncion();//this will work because ObjectFunction is inherited through all children
		//ObjectArray[i]->ActorFuncion();//this will not work because it's not inherited
		Object* obj = ObjectArray[i];
		
		/* note difference btwn STATIC and DYNAMIC casting*/
		//Actor* act = dynamic_cast<Actor*>(obj);//casting the object; if cast failed, will return null
		Actor* act = static_cast<Actor*>(obj);
		if (act) {
			act->ActorFunction();
		}
		//Pawn* pwn = dynamic_cast<Pawn*>(obj);
		Pawn* pwn = static_cast<Pawn*>(obj);
		if (pwn) {
			pwn->PawnFunction();
		}
	}

	delete ptr_to_obj;
	delete ptr_to_act;
	delete ptr_to_pwn;

	system("pause");
}

void Object::BeginPlay() {
	cout << "Object BeginPlay() called! \n\n";
}

void Actor::BeginPlay() {
	cout << "Actor BeginPlay() called! \n\n";
}

void Pawn::BeginPlay() {
	cout << "Pawn BeginPlay() called! \n\n";
}