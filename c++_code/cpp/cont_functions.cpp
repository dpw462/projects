#include <iostream>
using namespace std;

void Welcome(); 
char getYesNo();
void printResponse(char responseToPrint);
void askYesOrNoQuestion();

int main() {

	//asks user to enter y or n and return response
	askYesOrNoQuestion();
	system("pause");
}

void Welcome() {
	//welcome user to program
	cout << "Welcome!\n";
}

char getYesNo() {
	//get user input yes or no
	cout << "Please answer: y or n\n";
	//char variable to store response
	char response;
	//get input from user via keyboard
	cin >> response;
	
	return response;
}

void printResponse(char responseToPrint) {
	//print the response to the screen
	cout << "Your selection was: " << responseToPrint << endl;
}

void askYesOrNoQuestion() {
	//greet user
	Welcome();
	//create char variable and store result
	char ans = getYesNo();// getYesNo() gets a y or n from user
	//print response from user to screen
	printResponse(ans);
}