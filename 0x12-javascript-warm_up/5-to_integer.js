#!/usr/bin/node

const args = process.argv;
const num = Number.parseInt(args[2]);
if (args.length === 2 || !(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
