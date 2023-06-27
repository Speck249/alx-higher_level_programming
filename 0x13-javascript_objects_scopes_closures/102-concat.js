#!/usr/bin/node

const fs = require('fs');
const File1 = fs.readFileSync(process.argv[2]).toString();
const File2 = fs.readFileSync(process.argv[3]).toString();
const File3 = process.argv[4];
fs.writeFileSync(File3, File1 + File2);
