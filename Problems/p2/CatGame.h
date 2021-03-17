#pragma once
#include <iostream>
#include <conio.h>
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