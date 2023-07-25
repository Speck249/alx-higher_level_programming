#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(file, body, { encoding: 'utf-8' }, error => {
    if (error) {
      console.error(error);
      return;
    }

    console.log(file);
  });
});
