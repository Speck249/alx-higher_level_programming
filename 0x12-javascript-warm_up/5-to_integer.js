#!/usr/bin/node

const len = process.argv.length;
const res = parseInt(process.argv[2]);

if (len == 2 || (!res)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${res}`);
}
