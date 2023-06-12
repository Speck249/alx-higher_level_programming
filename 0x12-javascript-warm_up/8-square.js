#!/usr/bin/node

const len = process.argv.slice(2);

if (len === 0 || (!parseInt(len[0]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < len[0]; i++) {
    let j = 0;
    let res = '';
    while (j < len[0]) {
      res = res + 'X';
      j++;
    }
    console.log(res);
  }
}
