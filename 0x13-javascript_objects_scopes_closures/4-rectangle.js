#!/usr/bin/node

class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0) {
			this.width = w
			this.height = h
		}
	}

	print() {
		let rect = "";
		for (i = 0; i < this.width; i++) {
			rect = rect + 'X';
                }
                for (i = 0; i < this.height; i++) {
			console.log(rect)
		}
	}

	rotate() {
		const temp = this.width;
		this.width = this.height;
		this.height = temp;
	}

	double() {
		this.weight *= 2;
		this.height *= 2;

}

module.exports = Rectangle;
