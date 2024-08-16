#!/usr/bin/node

const mainSquare = require('./5-square.js');

class Square extends mainSquare {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let idx = 0; idx < this.width; idx++) {
      let square = ''
      for (let i = 0; i < this.height; i++) {
        square += c
      }
      console.log(square);
    }
  }
}

module.exports = Square;
