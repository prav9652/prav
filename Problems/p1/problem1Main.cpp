#include "dictionary.h"

Dictionary::Dictionary()
{
	word = "NONE";
	meaning = "NONE";
}

void Dictionary::assign(Dictionary dict[], int size)
{
	for (int i = 0; i < size; i++)
	{
		switch (i)
		{
		case 0:
			dict[i].word = "foo";
			dict[i].meaning = "A file";
			break;
		case 1:
			dict[i].word = "fooo";
			dict[i].meaning = "A long file";
			break;
		case 2:
			dict[i].word = "foooo";
			dict[i].meaning = "A long long file";
			break;
		case 3:
			dict[i].word = "fooooo";
			dict[i].meaning = "A long long long file";
			break;
		case 4:
			dict[i].word = "foooooo";
			dict[i].meaning = "A long long long long file";
			break;
		case 5:
			dict[i].word = "fooooooo";
			dict[i].meaning = "A long long long long long file";
			break;
		default:
			cout << "Sorry, there is no meaning for this word in the dictionary\n";
			break;
		}
	}
}

void Dictionary::search(string userInput, Dictionary dict[]) {
	for (int i = 0; i < 6; i++)
	{
		if (userInput == dict[i].word)
		{
			cout << "Meaning: " << dict[i].meaning << endl;
			return;
		}
		if (i == 6 - 1)
			cout << "Sorry, there is no meaning for this word in the dictionary\n";
	}
}

Dictionary::~Dictionary() {}

NewDictionary::NewDictionary() :Dictionary() {

}

int NewDictionary::countTotalLines(string fileName) {
	ifstream fin(fileName);
	int numberOfLines = 0;
	while (getline(fin, word))
		numberOfLines++;

	fin.close();
	return numberOfLines;
}

void NewDictionary::findMeaning(string userInput, string searchFileName) {
	int totalLines = countTotalLines(searchFileName + ".txt");
	ifstream finS(searchFileName + ".txt");
	int index = 0;
	word = userInput;
	if (word.length() > 2) {
		int counter = 0;

		while (!finS.eof()) {
			getline(finS, meaning);
			if (meaning.find("Word: " + word) != string::npos) {
				index = meaning.find("; ");
				meaning = meaning.substr(index + 2);
				cout << meaning << endl;
				break;
			}
			if (counter >= totalLines - 1)	
				goto invalid;

			counter++;
		}
	}
	else {
	invalid:
		cout << "Word is too short or Invalid word entered.\n";
	}
}


NewDictionary::~NewDictionary() {}


int main() {
	Dictionary dit[6];
	NewDictionary dict;
	string userInputWord;
	char retryChoice;
	dict.assign(dit, 6);
	do
	{
		cout << "Enter the word: ";
		cin >> userInputWord;
		dict.search(userInputWord, dit);
		dict.findMeaning(userInputWord, "synonym");
		dict.findMeaning(userInputWord, "antonym");

		cout << "\nDo you want to search again? (y/n): ";
		cin >> retryChoice;
	} while (retryChoice== 'Y' || retryChoice == 'y');
	
 return 0;
}
