#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUri, function (error, response, body) {
  const chars = JSON.parse(body).characters;

  for (let i = 0; i < chars.length; ++i) {
    request(chars[i], function (carErr, carRes, carBody) {
      console.log(JSON.parse(carBody).name);
    });
  }
});
