#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const output = JSON.parse(body);
  const tasksDone = output.filter(task => {
    return task.completed;
  });

  const userTasks = {};
  tasksDone.forEach(task => {
    if (userTasks[task.userId]) {
      userTasks[task.userId]++;
    } else {
      userTasks[task.userId] = 1;
    }
  });
  console.log(userTasks);
});
