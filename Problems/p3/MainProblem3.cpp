#include "Cuboid.h"
#include<math.h>

Point::Point() {
	x = y = z = 0;
}

void Point::setPoint(float m, float n, float o) {
	x = m;
	y = n;
	z = o;
}

float Point::getX() {
	return x;
}
float Point::getY() {
	return y;
}
float Point::getZ(){
	return z;
}

Point::~Point() {}

Line::Line() {
	start.setPoint(0, 0, 0);
	end.setPoint(0, 0, 0);
}

void Line::setLine(float Xstart, float Ystart, float Zstart, float Xend, float Yend, float Zend) {
	start.setPoint(Xstart, Ystart, Zstart);
	end.setPoint(Xend, Yend, Zend);
}

float Line::distance() {
	return sqrt(pow(start.getX() - end.getX(), 2)
		+ pow(start.getY() - end.getY(), 2) + pow(start.getZ() - end.getZ(), 2));
}

Line::~Line() {}

Rectangle::Rectangle() {
	length.setLine(0, 0, 0, 0, 0, 0);
	width.setLine(0, 0, 0, 0, 0, 0);
}

void Rectangle::setRectangle(Line l, Line w) {
	length = l;
	width = w;
}

float Rectangle::Area() {
	return length.distance() * width.distance();
}

float Rectangle::Area(Line l, Line w) {
	length = l;
	width = w;
	return length.distance() * width.distance();
}

Rectangle::~Rectangle() {}

Cuboid::Cuboid():r(), height() {
	
}

float Cuboid::surfaceArea(float l, float w, float h) {
	//2(lw) + 2(hl) + 2(hw)
	return 2 * l + 2 * w + 2 * h;
}

float Cuboid::volume(float l, float w, float h) {
	//l * w * h
	return l * w * h;
}

Cuboid::~Cuboid() {}



int main() {
	Line length, width, height;
	length.setLine(0, 0, 0, 0, 6, 0);
	width.setLine(0, 0, 0, 5, 0, 0);
	height.setLine(0, 0, 0, 0, 0, 4);

	Rectangle m;
	float areaL, areaW, areaH;
	m.setRectangle(length, width);
	areaL = m.Area();
	cout << "The area of first rectangle in the cuboid: " << areaL << endl;

	m.setRectangle(width, height);
	areaW = m.Area();
	cout << "The area of second rectangle in the cuboid: " << areaW << endl;

	m.setRectangle(height, length);
	areaH = m.Area();
	cout << "The area of third rectangle in the cuboid: " << areaH << endl;

	cout << endl;
	Cuboid c;
	cout << "The  Total Surface Area of cuboid is " << c.surfaceArea(areaL, areaW, areaH) << endl;

	cout << "The Volume of the cuboid is " << c.volume(length.distance(), width.distance(), height.distance()) << endl << endl;
	return 0;
}