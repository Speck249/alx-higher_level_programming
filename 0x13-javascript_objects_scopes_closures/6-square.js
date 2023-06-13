#!/usr/bin/node

const mainSquare = require('./5-square.js');

class Square extends mainSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let sq = '';
    for (let i = 0; i < this.width; i++) {
      sq = sq + c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(sq);
    }
  }
}

module.exports = Square;
