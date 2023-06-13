#!/usr/bin/node

exports.esrever = function (list) {
  const res = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    res[j] = list[i];
    j++;
  }
  return res;
};
