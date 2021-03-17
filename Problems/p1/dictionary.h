#pragma once
#include <iostream>
#include <string>
#include <fstream>
#include <cctype>
#pragma once
#include <iostream>

#include <cstdlib>
#include <ctime>

using namespace std;

class MotherCat
{
protected:
	int catSpeed;
	char board[19][19];
	int XcatPosition, YcatPosition;
	char catSymbol;
	int score;

public:
	MotherCat();
	~MotherCat();
	void printBoard()const;
	void testMoves();
	void instructions();
};

class Kitten :
	public MotherCat
{
private:
	int kittenSpeed;
	char kittenSymbol;
	int XkittenPosition, YkittenPosition;

public:
	void updateKittenPosition();
	void startGame();
	void kittenCaught();
	Kitten();
	~Kitten();
};
using namespace std;

class Dictionary
{
protected:
	string word;
	string meaning;

public:
	Dictionary();
	void assign(Dictionary x[], int size);
	void search(string userInput, Dictionary x[]);
	~Dictionary();
};

class NewDictionary :public Dictionary {
public:
	NewDictionary();
	int countTotalLines(string);
	void findMeaning(string, string);
	~NewDictionary();
};