#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0
  if (list.length === 0) {
    return 0
  }
  for (let val of list) {
    if (val === searchElement) {
      counter += 1
    }
  }
  return counter
}
