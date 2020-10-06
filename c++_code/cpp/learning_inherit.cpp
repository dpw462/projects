#include <iostream>
#include <string>
using namespace std;

class Animal {
public:
	Animal();//call constructor
	Animal(string name, int age, int num_limbs);//overload of constructor
	
	string Name;
	int Age;
	int Num_Limbs;

	void Report();

};

class Dog : public Animal {
public:
	Dog();
	Dog(string name, int age, int num_limbs);

	void Speak();
};

class Corgi : public Dog {
public:
	Corgi();
	Corgi(string name, int age, int num_limbs);
	
	void CorgiTalk();
};

int main() {
	/*	
	Animal animal;
	animal.Report();
	Animal animal_2("Cheetah", 7, 5);
	//animal_2.Report();
	*/
	Dog dog("Spot",4,5);
	//dog.Speak();
	Corgi corgi("Lucy",3,5);
	corgi.CorgiTalk();
	Dog dog2("Rex", 5, 4);
	system("pause");
}

Animal::Animal() {
	cout << "An ANIMAL is born!\n";
	//initialize default values
	Name = "DEFAULT";
	Age = 2;
	Num_Limbs = 4;
}

//overload constructor; two different ways to initialize
Animal::Animal(string name, int age, int num_limbs): Name(name), Age(age), Num_Limbs(num_limbs) {
	/*one way to initialize, the other is above in declaration using : (initializer list)
	Name = name;
	Age = age;
	Num_Limbs = num_limbs;
	*/
	//call Report() from constructor itself
	Report();
}

void Animal::Report() {
	cout << endl;
	cout << "Name: " << Name << endl;
	cout << "Age: " << Age << endl;
	cout << "Limbs: " << Num_Limbs << endl;
	//cout << endl;
}

Dog::Dog() {
	cout << "A DOG is born!\n";
}

Dog::Dog(string name, int age, int num_limbs): Animal(name, age, num_limbs) {
	//by keeping below and not using the : notation above, you will get the constructor that takes no args
	//Animal(name, age, num_limbs);
}

Corgi::Corgi(string name, int age, int num_limbs): Dog(name, age, num_limbs) {

}

void Dog::Speak(){
	cout << "WOOF!" << endl;
}

void Corgi::CorgiTalk() {
	cout << "I'm a corgi with cute ears!\n";
}