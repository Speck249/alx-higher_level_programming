#!/usr/bin/node

const max = Number.parseInt(process.argv[2]);
if (!(max)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < max; i++) {
    console.log('C is fun');
  }
}
