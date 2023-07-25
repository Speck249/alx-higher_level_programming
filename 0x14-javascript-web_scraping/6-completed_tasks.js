#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const userTasks = {};
  const output = JSON.parse(body);

  for (let counter = 0; counter < output.length; counter++) {
    if (output[counter].completed === true) {
      if (userTasks[output[counter].userId] === undefined) {
        userTasks[output[counter].userId] = 0;
      }
      userTasks[output[counter].userId]++;
      }
    }
   console.log(userTasks);
});
