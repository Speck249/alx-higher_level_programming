#!/usr/bin/node

const size = Number.parseInt(process.argv[2]);
if (!(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
