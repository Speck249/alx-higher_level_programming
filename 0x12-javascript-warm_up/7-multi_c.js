#!/usr/bin/node

const num_occurence = process.argv[2];

if (!(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let idx = 0; idx < num_occurence; idx++) {
    console.log('C is fun');
  }
}
