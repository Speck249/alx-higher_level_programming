#!/usr/bin/node

const args = process.argv;
let a = Number.parseInt(args[2]);
let b = Number.parseInt(args[3]);

function add (a, b) {
  return a + b;
}

console.log(add(a, b));
