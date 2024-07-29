#!/usr/bin/node

let args = process.argv.slice(2).map(Number);
if (args.length === 0) {
  console.log(0);
}
args = args.sort((a, b) => (a - b));
console.log(args[args.length - 2]);
