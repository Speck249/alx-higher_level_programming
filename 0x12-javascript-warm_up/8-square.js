#!/usr/bin/node

square_size = parseInt(process.argv[2]);

if (!(parseInt(square_size))) {
  console.log('Missing size');
} else {
  for (idx = 0; idx < square_size; idx++) {
    square = Array(square_size).fill('X').join('')
    console.log(square)
  }
}
