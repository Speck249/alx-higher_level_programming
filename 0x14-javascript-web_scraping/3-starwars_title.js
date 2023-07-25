#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';
request(url, function (error, response, body) {
  if (error == null) {
    const result = JSON.parse(body);
    console.log(result.title);
  }
});
