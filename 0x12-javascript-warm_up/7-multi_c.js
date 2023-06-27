#!/usr/bin/node

const len = process.argv.length;

if (len === 2) {
  console.log('Missing number of occurrences');
} else {
  const args = process.argv.slice(2);
  for (let i = 0; i < args; i++) {
    console.log('C is fun');
  }
}
