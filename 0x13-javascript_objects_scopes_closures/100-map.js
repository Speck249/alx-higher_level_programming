#!/usr/bin/node

const list = require('./100-data.js').list;

const res = list.map((y, i) => y * i);
console.log(list);
console.log(res);
