#include "CatGame.h"
#define CLS system("cls")

MotherCat::MotherCat()
{
	XcatPosition = YcatPosition = 9;
	catSymbol = 'M';
	catSpeed = 2;
	score = 0;
	for (int i = 0; i < 19; i++)
	{
		for (int j = 0; j < 19; j++)
		{
			board[i][j] = '-';
		}
	}
	board[XcatPosition][YcatPosition] = catSymbol;
}

void MotherCat::instructions() {
	cout << "Welcome to this cat chasing game.\n";
	cout << "You are playing as mother cat. Mother Cat Symbol: M\n";
	cout << "You have to chase the kitten. Kitten Symbol: K\n";
	cout << "Use the arrow keys on the number pad to move mother cat.\n";
	cout << "NOTE: Sometimes, Mom cat can overlap the kitten because of its 2x speed than kitten speed.\n";
	cout << "Press 'esc' or 's' to stop the game.\n";
	cout << "Your Score: " << score << endl;
}

void MotherCat::printBoard()const {
	for (int i = 0; i < 19; i++)
	{
		cout << "\t\t";
		for (int j = 0; j < 19; j++)
		{
			cout << board[i][j] << " ";
		}
		cout << endl;
	}
}

Kitten::Kitten() : MotherCat()
{
	kittenSymbol = 'K';
	kittenSpeed = catSpeed / 2;
	XkittenPosition = YkittenPosition = rand() % 19;
	while (XkittenPosition == 9 && YkittenPosition == 9)
		XkittenPosition = YkittenPosition = rand() % 19;
	
	board[XkittenPosition][YkittenPosition] = kittenSymbol;
}

void Kitten::updateKittenPosition() {
	int randPos = rand() % 4 + 1;
	switch (randPos)
	{
	case 1:
		board[XkittenPosition][YkittenPosition] = '-';
		if (XkittenPosition == 0)
			XkittenPosition = 18;
		XkittenPosition -= kittenSpeed;
		board[XkittenPosition][YkittenPosition] = kittenSymbol;
		break;
	case 2:
		board[XkittenPosition][YkittenPosition] = '-';
		if (XkittenPosition == 18)
			XkittenPosition = 0;
		XkittenPosition += kittenSpeed;
		board[XkittenPosition][YkittenPosition] = kittenSymbol;
		break;
	case 3:
		board[XkittenPosition][YkittenPosition] = '-';
		if (YkittenPosition == 0)
			YkittenPosition = 18;
		YkittenPosition -= kittenSpeed;
		board[XkittenPosition][YkittenPosition] = kittenSymbol;
		break;
	case 4:
		board[XkittenPosition][YkittenPosition] = '-';
		if (YkittenPosition == 18)
			YkittenPosition = 0;
		YkittenPosition += kittenSpeed;
		board[XkittenPosition][YkittenPosition] = kittenSymbol;
		break;
	default:
		break;
	}
}

void Kitten::kittenCaught() {
	if (XcatPosition == XkittenPosition && YcatPosition == YkittenPosition)
	{
		CLS;
		board[XcatPosition][YcatPosition] = '$';
		score += 10;
		printBoard();
		cout << "You caught the kitten.\n";
		cout << "Press enter twice to continue the game\n";
		getch();
		board[XcatPosition][YcatPosition] = '-';
		XcatPosition = YcatPosition = 9;
		board[XcatPosition][YcatPosition] = catSymbol;
	}
}


void Kitten::startGame() {
	while (true) {
		char ch;
		instructions();
		printBoard();
		if (kbhit()) {
			kittenCaught();
			ch = getch();

			if (int(ch) == 27 || (int(ch) == 83 || int(ch) == 115))	//stopping the game when esc, S, or s is pressed.
				break;
			else if (int(ch) == 56)//up
			{
				board[XcatPosition][YcatPosition] = '-';
				if (XcatPosition == 0 || XcatPosition == 1)
					XcatPosition = 18;

				XcatPosition -= catSpeed;
				board[XcatPosition][YcatPosition] = catSymbol;
			}
			else if (int(ch) == 50)//down
			{
				board[XcatPosition][YcatPosition] = '-';
				if (XcatPosition == 17 || XcatPosition == 18)
					XcatPosition = 0;

				XcatPosition += catSpeed;
				board[XcatPosition][YcatPosition] = catSymbol;
			}
			else if (int(ch) == 54)//right
			{
				board[XcatPosition][YcatPosition] = '-';
				if (YcatPosition == 17 || YcatPosition == 18)
					YcatPosition = 0;

				YcatPosition += catSpeed;
				board[XcatPosition][YcatPosition] = catSymbol;
			}
			else if (int(ch) == 52)//left
			{
				board[XcatPosition][YcatPosition] = '-';
				if (YcatPosition == 0 || YcatPosition == 1)
					YcatPosition = 18;

				YcatPosition -= catSpeed;
				board[XcatPosition][YcatPosition] = catSymbol;
			}
			else
			{
				cout << "\nWrong Key Pressed.\n";
			}
			CLS;
			kittenCaught();
			updateKittenPosition();
			//cout << "\nKey pressed= " << ch << endl;
		}
	}
}

void MotherCat::testMoves()		//use this function to check the movement of mother cat
{
	char ch;
	while (true) {
		printBoard();
		if (kbhit()) {

			ch = getch();

			if (int(ch) == 27)
				break;
			else if (int(ch) == 56)//up
			{
				board[XcatPosition][YcatPosition] = '-';
				if (XcatPosition == 0 || XcatPosition == 1)
					XcatPosition = 18;

				XcatPosition -= catSpeed;
				board[XcatPosition][YcatPosition] = catSymbol;
			}
			else if (int(ch) == 50)//down
			{
				//system("CLS");
				board[XcatPosition][YcatPosition] = '-';
				if (XcatPosition == 17 || XcatPosition == 18)
					XcatPosition = 0;

				XcatPosition += catSpeed;
				board[XcatPosition][YcatPosition] = catSymbol;
				//printBoard();
			}
			else if (int(ch) == 54)//right
			{
				board[XcatPosition][YcatPosition] = '-';
				if (YcatPosition == 17 || YcatPosition == 18)
					YcatPosition = 0;

				YcatPosition += catSpeed;
				board[XcatPosition][YcatPosition] = catSymbol;
			}
			else if (int(ch) == 52)//left
			{
				board[XcatPosition][YcatPosition] = '-';
				if (YcatPosition == 0 || YcatPosition == 1)
					YcatPosition = 18;

				YcatPosition -= catSpeed;
				board[XcatPosition][YcatPosition] = catSymbol;
			}
			else
			{
				cout << "\nWrong Key Pressed.\n";
			}

			CLS;
			cout << "\nKey pressed= " << ch << endl;
		}
	}

}

MotherCat::~MotherCat() {}

Kitten::~Kitten() {}

/*
Problem 2: Write a C++ program and algorithm for a class inheritance game where a kitten
with random position in the gameboard is to be caught by its mother cat whose initial
position is center to board and speed to particular direction a little higher than the kitten.
The class member functions include a draw function where the mother cat stays at the middle.
The direction is measured by the input function when say press ‘4’ means LEFT, ‘6’ means RIGHT,
‘8’ means UP,  ‘2’ means DOWN and ‘s’ means STOP. Use a score as the mother cat catches her kitten.
Change the coordinates of the kitten and mother cat to zero, if they touch the wall.(Marks 30)

Note: Use #include<conio.h> for console I/O and functions kbhit() which returns true
if key board is pressed and getch() which returns ASCII value of the key pressed.
*/

int main() {
	srand(time(0));
	Kitten k;

	//MotherCat m;
	//m.playGame();

	k.startGame();

	system("pause");
	return 0;
}

