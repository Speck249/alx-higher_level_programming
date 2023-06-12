#!/usr/bin/node
const len = process.argv.slice(2);
if (len === 0) {
  console.log('No argument');
} else if (len === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
