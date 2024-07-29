#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
  for (const key in myObject) {
    if (key === 'value') {
      let val = myObject[key];
      myObject[key] = val += 1;
    }
  }
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
