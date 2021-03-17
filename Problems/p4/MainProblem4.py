#include "ghost.h"

int GhostGame::ghostPresence = rand() % 4 + 1;

GhostGame::GhostGame()
{
	ghostPresence = 0;
	score = 0;
	playerSelection = 0;
	for (int i = 0; i < 4; i++)
		door[i] = false;
}

GhostGame::~GhostGame() {}

void GhostGame::generateGhost()
{
	for (int i = 0; i < 4; i++)
		door[i] = false;
	ghostPresence = rand() % 4 + 1;
	switch (ghostPresence)
	{
	case 1:
		door[0] = true;
		break;
	case 2:
		door[1] = true;
		break;
	case 3:
		door[2] = true;
		break;
	case 4:
		door[3] = true;
		break;
	default:
		break;
	}
}

void GhostGame::playGame()
{
	score = 0;
	cout << setw(70) << setfill('_') << "_\n";
	while (true)
	{
		generateGhost();
		playerSelection = rand() % 4 + 1;

		if (!door[playerSelection - 1]) {
			score += 10;
			cout << "\t-> Player selected door #" << playerSelection << ". (Ghost was in door #" << ghostPresence << ".)\n";
		}
		else {
			cout << "\t-> Player selected door #" << playerSelection << ". (Ghost was in door #" << ghostPresence << ".)\n";
			cout << ">>> GAME OVER <<<\n";
			break;
		}
	}
	cout << "Player score is " << score << endl;
	cout << setw(70) << setfill('_') << "_\n";
	cout << setw(70) << setfill('*') << "*\n";
}

void GhostGame::selectWinner(GhostGame &p2) {
	if (score > p2.score)
		cout << "\n>>>> PLAYER #1 WINS!\n\n";
	else if (score < p2.score)
		cout << "\n>>>> PLAYER #2 WINS!\n\n";
	else
		cout << "\n>>>> It's a Draw. Both players have same scores.\n\n";
}


int GhostGamev2::goodGhostPosition = rand() % 4 + 1;

GhostGamev2::GhostGamev2() :GhostGame() {

}

GhostGamev2::~GhostGamev2() {
}

void GhostGamev2::generateGoodGhost() {
	for (int i = 0; i < 4; i++)
		door[i] = false;
	goodGhostPosition = rand() % 4 + 1;
	switch (goodGhostPosition)
	{
	case 1:
		door[0] = true;
		break;
	case 2:
		door[1] = true;
		break;
	case 3:
		door[2] = true;
		break;
	case 4:
		door[3] = true;
		break;
	default:
		break;
	}
}

void GhostGamev2::playGame()
{
	score = 0;
	cout << setw(90) << setfill('_') << "_\n";
	while (true)
	{
		generateGhost();
		playerSelection = rand() % 4 + 1;

		if (!door[playerSelection - 1]) {
			generateGoodGhost();
			score += 10;
			cout << "\t-> Player selected door #" << playerSelection << ". (Ghost was in door #" << ghostPresence
				<< "; Good Ghost was in door #" << goodGhostPosition << ".)\n";

			if (playerSelection == goodGhostPosition)	//this block adds 100 points to the score
			{
				score += 100;
				cout << "~> Player found good ghost!(+100 POINTS)\n";
			}
		}
		else {
			cout << "\t-> Player selected door #" << playerSelection << ". (Ghost was in door #" << ghostPresence
				<< "; Good Ghost was in door #" << goodGhostPosition << ".)\n";
			if (playerSelection == goodGhostPosition)
			{
				score += 100;
				cout << "~> Player found good ghost!(+100 POINTS)\n"
					<< "Unfortunately, bad ghost was in the same door :\n";
			}
			cout << "\n>>> GAME OVER <<<\n";
			break;
		}
	}
	cout << "Player score is " << score << endl;
	cout << setw(90) << setfill('_') << "_\n";
	cout << setw(90) << setfill('*') << "*\n";
}


int main() {
	srand(time(0));
	GhostGamev2 player1, player2;

	cout << setw(90) << setfill('/') << ' ' << endl;
	cout << "\tWelcome to the Ghost Game v2.0\n";
	cout << "\tThe game now contains new ghost which rewards 100 points if you find it.\n";
	cout << "\tNOTE: If a player finds the good ghost and bad ghost in same door,\n"
		<< "\t      player will still get +100.\n";
	cout << setw(90) << setfill('\\') << ' ' << endl;
	

	cout << "\nPLAYER #1: \n";
	player1.playGame();
	cout << "\n";

	cout << "\nPLAYER #2: \n";
	player2.playGame();
	cout << "\n";

	player1.selectWinner(player2);
	return 0;
}