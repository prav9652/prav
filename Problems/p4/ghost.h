#pragma once
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <iomanip>

using namespace std;

class GhostGame
{
protected:
	static int ghostPresence;
	int playerSelection;
public:
	bool door[4];
	int score;

	void generateGhost();
	void playGame();
	void selectWinner(GhostGame &p2);
	GhostGame();
	~GhostGame();
};

class GhostGamev2 :public GhostGame
{
public:
	GhostGamev2();
	~GhostGamev2();
	void generateGoodGhost();
	void playGame();

private:
	static int goodGhostPosition;
};