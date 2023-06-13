#!/usr/bin/node

const mainSquare = require('./5-square.js');

class Square extends mainSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
	    let sq = '';
	  for (let i = 0; i < this.height; i++) {
		  sq = sq + c;
	  }
    console.log(sq);
    }
  }
}

module.exports = Square;
