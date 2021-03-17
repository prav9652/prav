#pragma once
#include <iostream>

using namespace std;

class Point
{
public:
	Point();
	void setPoint(float, float, float);
	float getX();
	float getY();
	float getZ();
	~Point();

private:
	float x, y, z;
};

class Line
{
public:
	Line();
	void setLine(float, float, float, float, float, float);
	float distance();
	~Line();

private:
	Point start, end;
};

class Rectangle
{
public:
	Rectangle();
	void setRectangle(Line l, Line w);
	float Area();
	float Area(Line l, Line w);
	~Rectangle();

private:
	Line length;
	Line width;
};

class Cuboid
{
public:
	Cuboid();
	float surfaceArea(float, float, float);
	float volume(float, float, float);
	~Cuboid();

private:
	Rectangle r;
	Line height;
};


