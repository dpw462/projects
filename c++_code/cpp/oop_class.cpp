#include <iostream>
#include <string>
using namespace std;

//structs and class basically the same except struct is automatically public
struct Cat {
	Cat();
	int age;
	float health;
	void meow();
};

Cat::Cat() {
	cout << "A new cat is born!" << endl;
	
	age = 3;
	health = 75.f;
	
	meow();
}

void Cat::meow(){
	cout << "My age is: " << age << endl;
	cout << "My health is: " << health << endl;
}

class Dog {

public:

	Dog();

	string Name;
	int age;
	float health;

	void Bark();
};


int main() {

	Cat cat;
	
	cat.age += 5;
	cat.meow();
		
	Dog dog;

	cout << dog.Name << endl;
	cout << dog.age << endl;
	cout << dog.health << endl;
	
	dog.Name = "Sam";
	dog.age = 14;
	dog.health = 50;

	cout << dog.Name << endl;
	cout << dog.age << endl;
	cout << dog.health << endl;
	
	system("pause");
}

//for constructor, do not need return type; all else, you do
Dog::Dog() {
	Bark();
	Name = "Default name";
	age = 10;
	health = 100.f;
}

void Dog::Bark() {
	cout << "WOOF!" << endl;
}
