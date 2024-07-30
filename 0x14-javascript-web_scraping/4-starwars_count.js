#!/usr/bin/node

const request = require('request');

const cId = 18;

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  }

  const filmData = JSON.parse(body);

  let count = 0;
  filmData.results.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${cId}/`)) {
      count++;
    }
  });

  console.log(count);
});
