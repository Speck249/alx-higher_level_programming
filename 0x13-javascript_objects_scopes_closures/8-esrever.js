#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = []
  if (list.length === 0) {
    return []
  }
  for (let idx = list.length - 1; idx >= 0; idx--) {
    reversedList.push(list[idx]);
  }
  return reversedList;
}
