#!/usr/bin/node

let args = process.argv.sort();
let maxNum, maxIndex;
maxNum = args[2];
if (args.length < 4) {
  console.log(0);
} else {
  for (i = 3; i <= args.length; i++) {
    if (args[i] > maxNum) {
      maxNum = args[i];
      maxIndex = i;
    }
  }
  console.log(args[maxIndex - 1]);
}
