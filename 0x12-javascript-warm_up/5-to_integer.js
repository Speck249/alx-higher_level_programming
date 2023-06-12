#!/usr/bin/node

const len = process.argv.length;
const args = process.argv.slice(2);

if (len === 2 || (!parseInt(args))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args));
}
