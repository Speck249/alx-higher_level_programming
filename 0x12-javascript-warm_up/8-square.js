#!/usr/bin/node

const len = process.argv.slice(2);

if (len === 0 || (!parseInt(len[0]))) {
  console.log('Missing size');
} else {
	let sq = "";
	for (i = 0; i < len[0]; i++) {
		sq = sq + 'X';
        }
        for (i = 0; i < len[0]; i++) {
		console.log(sq)
        }
}
