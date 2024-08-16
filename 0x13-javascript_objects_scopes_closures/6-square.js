#!/usr/bin/node

const mainSquare = require('./5-square.js');

class Square extends mainSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let square = '';
    for (let i = 0; i < this.width; i++) {
      square += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(square);
    }
  }
}

module.exports = Square;
