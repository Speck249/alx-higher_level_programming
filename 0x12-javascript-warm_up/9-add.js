#!/usr/bin/node

const len = process.argv.slice(2);
const a = len[0];
const b = len[1];

function add (a, b) {
  if (len < 2) {
    return NaN;
  } else {
    return a + b;
  }
}

console.log(add(parseInt(a), parseInt(b)));
