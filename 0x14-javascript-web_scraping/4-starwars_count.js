#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = 18;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const output = JSON.parse(body);
  const apiUrl = 'https://swapi-api.alx-tools.com/api/people/' + characterId + '/';
  const movies = output.results.filter(movie => {
    return movie.characters.includes(apiUrl);
  });

  console.log(movies.length);
});
