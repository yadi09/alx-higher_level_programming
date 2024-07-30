#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, respons) {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('code:', respons.statusCode);
  }
});
